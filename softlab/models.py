from django.db import models

# Create your models here.
class Friend(models.Model):
    # NICK NAME should be unique
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    hobbies = models.CharField(max_length = 250)
    
    lives_in = models.CharField(max_length=150, null = True, blank = True)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name