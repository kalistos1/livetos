from django import forms
from. models import ContactMessage



class ContactMessageForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields =('name','email','subject','body')
    
    def __init__(self, *args, **kwargs):
        super(ContactMessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control form-control-lg ', 'placeholder': 'Name',})
        self.fields['email'].widget.attrs.update({'class' : 'form-control form-control-lg ', 'placeholder': 'Email',})
        self.fields['subject'].widget.attrs.update({'class' : 'form-control-lg', 'placeholder': 'Subject',})
        self.fields['body'].widget.attrs.update({'class' : 'form-control-lg', 'placeholder': 'Message',})
