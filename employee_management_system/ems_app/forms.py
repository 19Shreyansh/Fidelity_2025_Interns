from django import forms
from ems_app.models import Profile

# class ContactForm(forms.Form):
#     name=forms.CharField(max_length=100,required=True)
#     email=forms.EmailField(max_length=100,required=False)
#     message=forms.CharField(max_length=1000)

class ProfileForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Profile
        fields='__all__'

# class LoginForm(forms.Form):
    # eid = forms.CharField(max_length=10)
    # password = forms.CharField(widget=forms.PasswordInput)