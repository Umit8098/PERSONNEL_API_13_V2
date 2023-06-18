from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    image = models.ImageField(upload_to='images',default='avatar.png', height_field=None, width_field=None, max_length=None)
    about = models.TextField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        # return self.user.username
        # return self.user.first_name
        return f'{self.user.username} - {self.user.first_name}'
