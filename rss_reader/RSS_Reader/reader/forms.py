from .models import RSS_Reader_Model
from   django import  forms

class Rss_Form(forms.ModelForm):
     # url=forms.CharField(label="hello",widget=forms.URLField(attrs={"class":"form-control","placeholder":"tweet something"}))
     class Meta:
         model=RSS_Reader_Model
         fields=["url"]

     def __init__(self, *args, **kwargs):
         super(Rss_Form, self).__init__(*args, **kwargs)
         self.fields['url'].widget.attrs.update({
             'id': 'url',
             'class': 'form-control',
             'name': 'url',
             'placeholder': 'Enter URL',


         })

     # def clean_url(self):
         # print(self.cleaned_data.get("url"),"dshfdfldskfjsdofdjoi")

