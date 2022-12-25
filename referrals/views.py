from django.shortcuts import render
from referrals.models import  Referral

# Create your views here.
def referals(request, *args, **kwargs):
    template = "pages/signup-ref.html"
    referral = str(kwargs.get('ref_code'))
    try:
       referrer = Referral.objects.get(referral_code = referral)
       request.session['ref_profile'] = referrer.id
     
    except:
        pass
  
    return render(request, template)