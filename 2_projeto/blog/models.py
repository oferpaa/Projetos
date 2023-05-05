from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title