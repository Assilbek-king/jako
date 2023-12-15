from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.


class Diagram(models.Model):
    title = models.CharField(max_length=100)
    percent = models.IntegerField(default=0 )


    def __str__(self):
        return f'{self.title} {self.percent}'

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    card_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    invest_sum = models.IntegerField(blank=True,default=0)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.email} - {self.name} {self.second_name}"