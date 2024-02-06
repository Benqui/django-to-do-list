from django.db import models

# Create your models here.
class Task(models.Model):
    TODO = "TO DO"
    COMPLETED = "COMPLETED"
    INPROGRESS = "IN-PROGRESS"
    STATUS_CHOICES = [ (TODO, 'TO DO'),(COMPLETED,'COMPLETED'),(INPROGRESS, 'IN-PROGRESS') ]
    
    title = models.CharField(max_length = 50)
    description = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add = True)
    due_date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length= 50, choices=STATUS_CHOICES, null=True, blank=True,default= TODO)
    def __str__(self) -> str:
        return self.title
