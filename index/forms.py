from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

""" usercreationform is inbuilt class which created basic form with validations if we want give extra fields give in fields() but
 in djnago  User for authentication/registration process so only these fields are given no extra fields are given"""

class myform(UserCreationForm):
    class Meta:
        model = User
        fields =('username','email','first_name','last_name','password1','password2')