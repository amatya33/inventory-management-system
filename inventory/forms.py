from django import forms
from .models import * 

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = "__all__"
        # fields = ('type', 'price', 'status', 'issues')

class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = "__all__" 
        # fields = ('type', 'price', 'status', 'issues')


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = "__all__"
        # fields = ('type', 'price', 'status', 'issues')


