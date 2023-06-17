from django.db import models
import mimetypes

class File(models.Model):
    FILE_TYPES = [
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('application', 'Application'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='files/')
    file_type = models.CharField(max_length=15, choices=FILE_TYPES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        file_path = self.file.path
        file_type, _ = mimetypes.guess_type(file_path)
        if file_type:
            self.file_type = file_type.split('/')[0]
        super().save(*args, **kwargs)

