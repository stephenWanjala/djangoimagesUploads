# models.py
import os

from django.db import models


def get_image_mimetype(image_path):
    try:
        ext = get_file_extension(image_path)
        mime_type = f"image/{ext}"
        return mime_type
    except FileNotFoundError:
        print(f"Error: File '{image_path}' not found.")
        return None


def get_file_extension(file_path):
    _, ext = os.path.splitext(file_path)
    return ext[1:]


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    mimetype = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.image:
            self.image.name = self.image.name.split('/')[-1]  # Derive the image name from the filename
            self.mimetype = get_image_mimetype(self.image.path)  # Get and store the mimetype of the image
        super(UploadedImage, self).save(*args, **kwargs)
