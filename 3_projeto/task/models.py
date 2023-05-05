from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    STATUS_OPTIONS = (
        ('concluded', 'Concluded'),
        ('pending', 'Pending'),
        ('postponed', 'Postponed'),
    )

    PRIORITY_OPTIONS = (
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    data_post = models.DateField(default=timezone.now)
    priority = models.CharField(
        max_length=25, choices=PRIORITY_OPTIONS, default='medium')
    status = models.CharField(
        max_length=25, choices=STATUS_OPTIONS, default='pending')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
