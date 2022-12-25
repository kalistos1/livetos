from django import forms
from django.contrib.auth import get_user_model
user = get_user_model
from . models import Faq


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields =('title','question','answer')

    def __init__(self, *args, **kwargs):
        super(FaqForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['question'].widget.attrs.update({'class':'form-control'})
        self.fields['answer'].widget.attrs.update({'class':'form-control'})
