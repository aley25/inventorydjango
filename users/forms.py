from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(max_length=80, label='User Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=80, label='Email', widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=80, label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=80, label='Second Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), max_length=80)

class LoginForm(forms.Form):    
    username = forms.CharField(max_length=80, label='User Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), max_length=80)