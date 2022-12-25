from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.http import url_has_allowed_host_and_scheme
from django.urls import resolve,reverse_lazy
from . forms import  SignUpForm, SignInForm,ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from referrals.models import Referral
#from investments.models import TranscationBalance
from . models import TempUrl
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from . models import Profile
from django.core.mail import EmailMessage
from django.contrib import messages
from . utils import *
import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
#from investments.models import Membership, UserMembership, TranscationBalance
from django.conf import settings
from .decorators import check_recaptcha

# Create your views here.


# sign in view
def sign_in(request):
    template ="pages/signin.html"
    if request.user.is_authenticated:
       return redirect('dashboard:analytics',request.user.username)

    if request.method == 'POST':

        form = SignInForm (request, data = request.POST) 
        if form.is_valid():
            cd = form.cleaned_data
            #next = request.GET.get('next') 
            #validate_next_url = url_has_allowed_host_and_scheme(next,allowed_hosts=None)
               
            user = authenticate(request,username=cd['username'], password=cd['password'])
                   
            if user is not None:
                if user.account_status == "2":
                    messages.error(request, 'Login failed. Your account has not been verified')
                    return redirect('authentication:signin')

                #if next is not None and validate_next_url == True:
                    # res = resolve (next)
                    # url_namespace = str (res.namespaces[0])+':'+str(res.url_name)
                    # st= f"\'{url_namespace}\'"
                    # print('lllllllllllllllllllllllllllllllllllll',st)
                    #return redirect(next)
                    

                if user is not None and user.is_authenticated and user.is_active: 
                    login(request,user)
                    username = user.username
                    return redirect('dashboard:profile',username)
                        
                else:
                    messages.error(request, 'Incorrect Username or Pasword')
                    return redirect('authentication:signin')
                               
        else:     
            messages.error(request, 'Incorrect Username or Pasword')
            return redirect('authentication:signin')
                                 
    else:  
        form = SignInForm()            
        context = {
                'form':form
                }      
        return  render(request, template, context)

    
    
# sign up view
def sign_up(request):
    template = "pages/signup.html"
    referrer_id = request.session.get('ref_profile')
 
  
    if request.method == 'POST':
        form =  SignUpForm(request.POST)
        
        if form.is_valid(): 

            cd = form.cleaned_data
            get_firstname = cd['first_name']
            get_lastname =cd['last_name']
            get_email = cd['email']
            get_username =cd['username']
            get_password1 = cd['password']
            get_password2 = cd['password2']
            get_t_and_c = cd['t_and_c']
           

                
            if User.objects.filter(username=get_username).exists():
                messages.error(request, 'Error username already Exists')
                return redirect('authentication:signup')

            elif User.objects.filter(email=get_email).exists():
                messages.error(request, 'Error Email already Exists')
                return redirect('authentication:signup')

            elif get_password1 != get_password2:
                messages.error(request, 'passwords does not match')
                return redirect('authentication:signup')
            elif get_t_and_c != True:
                messages.error(request, 'To Signup, agree to aour terms and conditions')
                return redirect('authentication:signup')
                
            else:
                
                try:
                    user = User.objects.create(password = make_password(get_password1), first_name = get_firstname, last_name = get_lastname, username = get_username, email = get_email)
  
                    # user = form.save() 
                  
                    get_membership = Membership.objects.get(membership_type='FREE')
                    membership_instance = UserMembership.objects.create(user=user, membership=get_membership)
                    transaction_balance = TranscationBalance.objects.create(user=user)

                    if referrer_id is not None:
                        recommended_by_referrer = Referral.objects.get(id = referrer_id)
        
                        registered_user = User.objects.get(id = user.id)
                        registered_referrer =  Referral.objects.get(user = registered_user)
                        registered_referrer.recommended_by = recommended_by_referrer.user
                        registered_referrer.save()
                       
                                       
                    link_hash = get_hash()            
                    current_date_and_time = datetime.datetime.now()
                    expiry_date = current_date_and_time + datetime.timedelta(hours = 24)

                    context = {
                        'hash': link_hash
                        } 

                    temp_url = TempUrl(url_hash=link_hash, user=user, expires=expiry_date)
                    temp_url.save()         
                    #send account registration email with user password
                    context = {
                        'name': get_firstname + " " + get_lastname,
                        'email':user.email,
                        'password': get_password1,
                        'hash': link_hash  
                        }

                    
                    send_email([user.email,], 'From OnicCapitals', 'emails/new_signup_email.html', context, 'Onic-Capitals <no-reply@oniccapitals.com>')
                
                    return render(request, "pages/registration_successful.html", context)
                
                except Exception as e:
                    return HttpResponse(e)
        else:
            print(form)
    form=SignUpForm()
    context ={
              'form': form
        }
    return render(request, template, context)
   
   
   
# user account verification   

def verify(request, hash):
    url = get_object_or_404(TempUrl, url_hash=hash, expires__gte=datetime.datetime.now())
    user = url.user
    user.account_status = "1" 
    user.t_and_c = True 
    user.save()
    context = {
        'user':user
    }
    messages.success(request,' Account was verified. To start earning, make sure to Subscribe to an investment Plan')
    return  redirect("dashboard:profile" )



# logout/signout view
def sign_out(request):
    logout(request)
    return redirect('core:index')
