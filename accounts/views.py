from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator

from .models import CustomUser
from .forms import CustomUserCreationForm, LoginForm

def signup(request):
    # prevent authenticated user from accessing this view
    if request.user.is_authenticated:
        return redirect('feed:feed')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            host_name = request.get_host()
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = f"{request.scheme}://{host_name}{reverse('accounts:activate', kwargs={'uidb64': uid, 'token': token})}"
            email_html_message = render_to_string('accounts/account_activation_email.html', {
                'user': user,
                'activation_link':activation_link,
            })
            # Send the activation email
            email = EmailMessage(
                'Account Activation',
                email_html_message,
                from_email='team@filserver.com',
                to=[user.email],
                
            )
            email.content_subtype="html"
            email.send()
            messages.info(request=request, message='Account Created. Check your Email to activate your Account!')
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request=request, message='You have Activated your Account. Kindly Login')
        return redirect('accounts:login')
    else:
        messages.error(request, 'Activation link is invalid!')
        return redirect('accounts:login')


def login_view(request):
    # prevent authenticated user from accessing this view
    if request.user.is_authenticated:
        return redirect('feed:feed')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('feed:feed')
                messages.warning(request, 'Account Not Activated. Check Your Email for Activation link!')
                return redirect('accounts:login')
            messages.error(request, 'Wrong Email or Password!')
            return redirect('accounts:login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')