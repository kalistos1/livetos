from django.shortcuts import render

# Create your views here.


def profile(request, username):
    template = "pages/profile.html"
    
    user = request.user
    
    context={
    'user':user,
        }
    return render(request, template,context)
    
    
    
def dashboard_analytics(request,username):
    template = "pages/dashboard_analytics.html"
    
    context ={
       'message':'hello'
    }
    return render(request, template, context)