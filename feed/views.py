from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
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

def download_file_view(request, file_id):
        file = get_object_or_404(File, id=file_id)
        file.downloads += 1
        file.save()
        return redirect(file.file.url)