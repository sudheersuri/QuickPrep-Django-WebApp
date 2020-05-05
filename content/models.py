from django.db import models

# Create your models here.
class Subjects(models.Model):
    subject = models.CharField(max_length=100,blank=False,unique=True)
    def __str__(self):
        return self.subject    

class Questions(models.Model):
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    question = models.TextField(blank=False)
    answer = models.TextField(blank=False)
    def __str__(self):
        return self.question    
