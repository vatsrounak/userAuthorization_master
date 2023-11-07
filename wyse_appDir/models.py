from django.db import models
from db_connection import db
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Add other fields as needed


    def __str__(self):
        return self.user.username
