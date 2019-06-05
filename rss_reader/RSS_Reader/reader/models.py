from django.db import models

# Create your models here.

# username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
class RSS_Reader_Model(models.Model):
    url=models.URLField();
