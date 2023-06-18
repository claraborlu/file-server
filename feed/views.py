from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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
            return redirect('feed:feed')
    else:
        form = FileUploadForm()
    
    return render(request, 'feed/upload_file.html', {'form': form})
