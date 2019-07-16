from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class MyForm(forms.Form):
    date = forms.DateField()
# from .models import Website

# class WebsiteForm(forms.ModelForm):
#     class Meta:
#         model = Website
#         # fields = ('MRP', 'Selling_Price', 'Brand', 'Title', 'Type', 'Model_Name', 'Date', 'Product_URL')
#         fields = ('Title',)