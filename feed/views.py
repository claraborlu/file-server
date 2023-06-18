from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.contrib import messages
from django.db.models import Q

from .forms import FileUploadForm
from .models import File

@login_required
def feed(request):
    files = File.objects.all()
    return render(request, 'feed/feed.html', {'files':files})
    
@staff_member_required
@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File Uploaded Successfully')
            return redirect('feed:feed')
    else:
        form = FileUploadForm()
    return render(request, 'feed/upload_file.html', {'form': form})

@login_required
def download_file_view(request, file_id):
        file = get_object_or_404(File, id=file_id)
        file.downloads += 1
        file.save()
        return redirect(file.file.url)
    
@login_required
def email_file_view(request, file_id):
    file = get_object_or_404(File, id=file_id)
    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email')
        
        email = EmailMessage(
            'File Email',
            'Please find the attached file.',
            'Team@FileServer.com',
            [recipient_email],
        )
        # Attach file to the email
        email.attach_file(file.file.path)
        email.send()
    
        # Update count of emails sent
        file.emails_sent += 1
        file.save()
        messages.success(request=request, message='File Emailed')
        return redirect('feed:feed')

@login_required
def search_view(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = File.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
    context = {
        'query': query,
        'files': results
    }
    return render(request, 'feed/search_results.html', context)


