from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    weeks_left = models.CharField(max_length=2, blank = True)

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        print(f'{self.end_date.isocalendar()[1] - self.start_date.isocalendar()[1]}')
        if self.weeks_left == "":
            self.weeks_left = f'{self.end_date.isocalendar()[1] - self.start_date.isocalendar()[1]}'
        super().save(*args, **kwargs)
