from django import forms
from .models import Join

# Create your models here.
class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ['fullname', 'email', 'zip_code']
    