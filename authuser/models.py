from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager

class User(AbstractUser):
    username = models.CharField(verbose_name='username', max_length = 255, unique=True)
    password = models.CharField(max_length=255)
    email   = models.EmailField()
    height  = models.IntegerField()
    weight  = models.IntegerField()
    ttl     = models.DateField()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.pk) + ' - ' + self.username

    def check_password(self, passwd):
        if (self.password == passwd):
            return True
        return False