

# Create your models here.
from django.db import models

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploaded_images/')
    prediction = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.prediction or "Unclassified Image"
