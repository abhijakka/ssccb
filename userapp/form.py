from django import forms
from adminapp.models import short_urlss
class UrlForm (forms. ModelForm):
    class Meta:
        model = short_urlss
        fields = ['long_url']