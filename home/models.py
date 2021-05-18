from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=200)
    email=models.EmailField()
    message = models.TextField()
    def __Str__(self):
        return self.name

class user_details:
    id : int
    name : str
    score : int