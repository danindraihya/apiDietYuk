from django.db import models
from authuser.models import User

class Kemajuan(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    kalori = models.IntegerField(max_length=255)
    streak = models.IntegerField(max_length=255)

    def __str__(self):
        return self.user_id

class Kalori(models.Model):
    kalori = models.IntegerField(max_length=255)
