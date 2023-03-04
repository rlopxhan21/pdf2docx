from django.db import models

class FileUpload(models.Model):
    uploaded_file = models.FileField(upload_to='uploaded_file/')
    converted_file = models.FileField(upload_to='converted_file/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File created at {self.created}"
    