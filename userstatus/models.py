from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Status(models.Model):
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        content = models.TextField()
        date_posted = models.DateTimeField(default=timezone.now)
        likes=models.ManyToManyField(User,related_name='likes',blank=True)
        totallikes= models.IntegerField()

        def __str__(self):
            return self.content
        def totallikes(self):
            return self.likes.count()


