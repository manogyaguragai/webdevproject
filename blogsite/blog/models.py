from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #Adding the users
from ckeditor_uploader.fields import RichTextUploadingField #Adding the ckeditor


class Post(models.Model):
    Title = models.CharField(max_length = 100)
    Content = RichTextUploadingField()
    Date_Posted = models.DateTimeField(default = timezone.now)
    # last_pdated = models.DateTimeField(auto_now = True)
    Author = models.ForeignKey(User, on_delete = models.CASCADE) #Adding post per user. Delete the post if the user is deleted. 
 

    def __str__(self):
        return self.Title