from django.db import models

class Task(models.Model):
  name = models.CharField(max_length=120, help_text='name')
  detail = models.TextField(help_text="details")
  toDate = models.DateTimeField("To Date")
  fromDate = models.DateTimeField("From Date")
  status = models.BooleanField(default=False)


 
  def __str__(self):
    return self.title