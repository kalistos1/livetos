from django.shortcuts import render,redirect
from faq.models import Faq
from testimonials.models import Testimoney
from.forms import ContactMessageForm
from django.contrib import messages
# Create your views here.


def index(request):
    template ="pages/index.html"
    faqs = Faq.objects.all()
    testimonies  = Testimoney.objects.all()
    
    if request.method =="POST":
        form = ContactMessageForm(request.POST)
       
        if form.is_valid():
            form.save()
            messages.success(request,"message was sent ")
            return redirect('core:index')
        else:
            messages.error(request, "Something went wrong Message was not sent")
            return render('core:index')
            
    form = ContactMessageForm()
    context = {
       'faqs':faqs,
       'testimonies':testimonies,
       'form':form,
    }
    return render(request,template,context)
    
    
 
# terms and conditions 
def privacy_policy(request):
    pass
    
    
    
# privacy policies    
def terms_and_conditions(request):
    pass