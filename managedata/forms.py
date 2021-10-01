from django import forms

from .models import DataInfo


class DataInfoForm(forms.ModelForm):
    class Meta:
        model = DataInfo
        fields = ('data_file', )