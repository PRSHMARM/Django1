from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator
# Create your models here.
import datetime

#from main.views import transfer


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(150),MinValueValidator(0)])
    email = models.CharField(max_length=256,validators=[EmailValidator],null=True, unique=True,default="enter username")
    password = models.CharField(max_length =6, default="enter password")
    mob = models.CharField(blank=True, null=True, max_length=10)
    address = models.CharField(blank=False, null=False, max_length=100)
    ACC_TYPE =(
        ('S','SAVINGS_ACCOUNT'),
        ('C','CURRENT_ACCOUNT'),
        ('F','FIXED_DEPOSITE'),
        ('R','RECURRING_DEPOSITE')
    )

    account_type = models.CharField(max_length=1, choices=ACC_TYPE)

    GENDERS =(
        ('F','FEMALE'),
        ('M','MALE')
    )

    gender = models.CharField(max_length=1, choices=GENDERS)

    balance = models.IntegerField(blank=False, null=True, validators=[MinValueValidator(500)])


    def __str__(self):
        return self.name


class Debit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    debit = models.IntegerField(blank=False, null=True)
    description = models.CharField(max_length=100, blank=False, null=False, default="BALANCE")
    date = models.DateField(("date"), default=datetime.date.today)
    time=models.DateField(("time"), default=datetime.time)



class Credit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credit = models.IntegerField(blank=False, null=True)
    description = models.CharField(max_length=100, blank=False, null=False, default="BALANCE")
    date = models.DateField(("date"), default=datetime.date.today)
    time = models.DateField(("time"), default=datetime.time)



class Transfer(models.Model):
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE,related_name='user')
    receiver = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='receiver')
    amount = models.IntegerField(blank=False, null=True,validators=[MinValueValidator(500)])
    date = models.DateField(("date"), default=datetime.date.today)



class Employee(models.Model):
    name_emp = models.CharField(max_length=100)
    age_emp = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(150),MinValueValidator(0)])
    email_emp = models.CharField(max_length=256,validators=[EmailValidator],null=True, unique=True,default="enter username")
    password_emp = models.CharField(max_length =6, default="enter password")
    mob_emp = models.CharField(blank=True, null=True, max_length=10)
    address_emp = models.CharField(blank=False, null=False, max_length=100)


