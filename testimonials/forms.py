from django import forms
from django.contrib.auth import get_user_model
user = get_user_model
from . models import Testimoney


class TestimoneyForm(forms.ModelForm):
    class Meta:
        model = Testimoney
        fields =('customer_name','customer_title','testimoney','customer_photo')

    def __init__(self, *args, **kwargs):
        super(TestimoneyForm, self).__init__(*args, **kwargs)
        self.fields['customer_name'].widget.attrs.update({'class':'form-control'})
        self.fields['customer_title'].widget.attrs.update({'class':'form-control'})
        self.fields['testimoney'].widget.attrs.update({'class':'form-control'})
        self.fields['customer_photo'].widget.attrs.update({'class':'form-control'})
