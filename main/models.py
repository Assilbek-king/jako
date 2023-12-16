from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime, timezone
# Create your models here.

# class Capital(models.Model):
#     sum = models.CharField(max_length=100,default=500000)
#     percent = models.IntegerField(default=0 , blank=True)
#
#
#     def __str__(self):
#         return f'{self.title} {self.percent}'

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
    invest_sum = models.FloatField(blank=True, default=0.0)

    # def save(self, *args, **kwargs):
    #     self.password = make_password(self.password)
    #     super().save(*args, **kwargs)

    # def check_password(self, raw_password):
    #     return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.name} {self.second_name}"

class UserProfit(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField(blank=True, default=datetime.now())
    profit = models.FloatField(blank=True, default=0.0)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.user.invest_sum += self.profit
    #     self.user.save()

    def __str__(self):
        return f"{self.user} - {self.date}"

class UserTransaction(models.Model):
    userprofit = models.ForeignKey(UserProfit, on_delete=models.CASCADE)
    date = models.DateField(blank=True, default=datetime.now())
    withdrawal = models.FloatField(blank=True, default=0.0)
    status = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.userprofit.user.invest_sum -= self.withdrawal
    #     self.userprofit.user.save()

    def Month(self):
        if self.date:
            return self.date.strftime("%B")
        return "No date entry"

    def __str__(self):
        return f"{self.userprofit} >>> снято {self.date}"




# class UserProfile(models.Model):
#     name = models.CharField(max_length=100)
#     second_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#     card_number = models.CharField(max_length=20)
#     password = models.CharField(max_length=255)
#     invest_sum = models.FloatField(blank=True,default=0.0)
#
#     def save(self, *args, **kwargs):
#         self.password = make_password(self.password)
#         super().save(*args, **kwargs)
#
#     def check_password(self, raw_password):
#         return check_password(raw_password, self.password)
#
#     def __str__(self):
#         return f" {self.name} {self.second_name}"
#
#
#
# class UserProfit(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     date = models.DateField(blank=True, default=datetime.now())
#     profit = models.FloatField(blank=True,default=0.0)
#
#     def __str__(self):
#         return f"{self.user} - {self.date}"
#
# class UserTransaction(models.Model):
#     userprofit = models.ForeignKey(UserProfit, on_delete=models.CASCADE)
#     date = models.DateField(blank=True, default=datetime.now())
#     withdrawal = models.FloatField(blank=True,default=0.0)
#
#     def Month(self):
#         if self.Date:
#             return self.Date.strftime("%B")
#         return "No date entry"
#
#     def __str__(self):
#         return f"{self.userprofit} >>> снято {self.date}"