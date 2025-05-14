from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    fio = models.CharField(max_length=120)
    phone = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Type_service(models.Model):
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name

class Order(models.Model):
   PAY_PAYMENT_CHOICES = {
       ('0',"Картой"),
       ('1', "Наличные"),
   }
   USLUGI_CHOICES = {
       ('0', "Новая"),
       ('1', "В работе"),
       ('2', "Выполнена"),
       ('3', "Отмена"),
   }
   address = models.CharField(max_length=100)
   phone = models.CharField(max_length=100)
   type = models.ForeignKey(Type_service, on_delete=models.CASCADE)
   date = models.DateField()
   time = models.TimeField()
   date_at = models.DateField(auto_now_add=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   comment = models.TextField(null=True, blank=True)
   pay_payment = models.CharField(
       max_length=2,
       choices=PAY_PAYMENT_CHOICES,
   )
   uslugi = models.CharField(
        max_length=1,
        choices=USLUGI_CHOICES,
        default="0",
    )