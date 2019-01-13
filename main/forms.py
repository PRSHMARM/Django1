from django import forms
from . import models
from django.forms import ModelForm


class UserForm(forms.ModelForm):
    class Meta:
        model =models.User
        fields = '__all__'


class userloginform(forms.ModelForm):
    class Meta:
        model = models.User
        fields =['email','password']



class credit_form(forms.ModelForm):
    class Meta:
        model = models.Credit
        fields = '__all__'

class debit_form(forms.ModelForm):
    class Meta:
        model = models.Debit
        fields = '__all__'

class transfer_form(forms.ModelForm):
    class Meta:
        model = models.Transfer
        fields = '__all__'

class signupemp_form(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields ='__all__'


class loginemp_form(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields =['email_emp','password_emp']


class editprofile_form(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['email','password','mob','address']