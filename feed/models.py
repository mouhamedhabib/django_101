from django.db import models
from sorl.thumbnail import ImageField


# Create your models here.
class post (models.Model):
    text = models.CharField(max_length=150, blank=True, null=False)
    image = ImageField()  
    def __str__(self) -> str:
        return self.text
    image = models.ImageField(upload_to='images/')  
    
    