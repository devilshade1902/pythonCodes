from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Pet_Store

class PetUserForm(UserCreationForm):
    class Meta:
        model = Pet_Store
        fields = ['fname', 'lname', 'username', 'email1', 'phone1', 'address1', 'password1', 'password2']
        # fields = [ 'phone1', 'address1', 'password1', 'password2']
        # widgets = {
        #     'fname': forms.TextInput(attrs={'class': 'form-control'}),
        #     'lname': forms.TextInput(attrs={'class': 'form-control'}),
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email1': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'phone1': forms.TextInput(attrs={'class': 'form-control'}),
        #     'address1': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class':'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        # }
