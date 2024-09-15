from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
