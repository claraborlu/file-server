from django.db import models
import mimetypes

class File(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='files/')
    file_type = models.CharField(max_length=15, blank=True, null=True)
    downloads = models.PositiveIntegerField(default=0)
    emails_sent = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at',]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        file_path = self.file.path
        file_type, _ = mimetypes.guess_type(file_path)
        if file_type:
            self.file_type = file_type.split('/')[0]
        super().save(*args, **kwargs)

