from django import forms
from django.contrib.auth.models import User
from .models import TicketMessage


class TicketMessageForm(forms.ModelForm):
    class Meta:
        model = TicketMessage
        fields= ('title','message','photo')

    def __init__(self, *args, **kwargs):
        super(TicketMessageForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control form-control-lg ', 'placeholder': 'Enter the subject of the ticket',}),
        self.fields['message'].widget.attrs.update({'class' : ' form-control', 'placeholder': 'ticket body',})
        self.fields['photo'].widget.attrs.update({'class' : 'form form-control'})