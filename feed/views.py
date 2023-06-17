from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import File

def feed(request):
    pdf_files = File.objects.filter(file_type='application')
    image_files = File.objects.filter(file_type='image')
    video_files = File.objects.filter(file_type='video')
    audio_files = File.objects.filter(file_type='audio')
    
    return render(request, 'feed/feed.html', {'pdf_files': pdf_files, 
                                                'image_files': image_files,
                                                'video_files': video_files, 
                                                'audio_files': audio_files, 
                                           })
    
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
