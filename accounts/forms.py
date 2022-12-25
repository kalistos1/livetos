from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from .models import Profile



class SignUpForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    password2 = forms.CharField(required = True)
    t_and_c = forms.BooleanField(required=True)

    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
          
            
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control', 'id':'name', 'placeholder':'First Name', 'id':'floatingInput', 'aria-describedby':'nameHelp'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control', 'id':'name', 'placeholder':'Last Name', 'id':'floatingInput','aria-describedby':'nameHelp'})
        self.fields['username'].widget.attrs.update({'class' : 'form-control', 'id':'name', 'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control', 'id':'email', 'placeholder':'Email'})
        self.fields['password'].widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form form-control px-5', 'id':'pass'})
        self.fields['password2'].widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class':'form form-control px-5', 'id':'re_pass'})
        self.fields['t_and_c'].widget.attrs.update({'class' : 'custom-control-label','id':'agree-term'})




        

class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email or Username', 
                                                    'class':'form form-control px-5', 'name':'email', 'id':'your_name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 
                                                    'class':'form form-control px-5', 'id':'your_pass'}))



class AddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    is_admin = forms.BooleanField(required=False)

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name','username', 'email', 'password', 'is_admin','account_status')

    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'First Name'}),
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'Last name'}),
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'}),
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'}),
        self.fields['password'].widget.attrs.update({'class':'form-control','placeholder':'Passsword'}),
        self.fields['is_admin'].widget.attrs.update({}),
        self.fields['account_status'].widget.attrs.update({'class':'form-control','placeholder':'Account Status'}),
       
       

       
class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields =('sex', 'crypto_address','phone','photo')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['sex'].widget.attrs.update({'class':'form-control',}),
        self.fields['crypto_address'].widget.attrs.update({'class':'form-control',}),
        self.fields['phone'].widget.attrs.update({'class':'form-control'}),
        self.fields['photo'].widget.attrs.update({'class':'form-control'}),

