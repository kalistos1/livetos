from email.policy import default
from re import L
from django.db import models
from accounts.models import User
from .utils import generate_ref_code

from django.utils.translation import gettext_lazy as _
# Create your models here.

class Referral(models.Model):
    user = models.ForeignKey(User ,on_delete= models.CASCADE , related_name="ref")
    referral_code = models.CharField (max_length = 12 , blank = True)
    recommended_by = models.ForeignKey(User, on_delete= models.CASCADE,  null=True, blank=True, related_name ="ref_by")
    created_at = models.DateField(auto_now = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user.username}-{self.referral_code}"

    def get_recommended_profiles(self):
        qs = Referral.objects.all()
        user_recommendations = []

        for referral in qs:
            if referral.recommended_by  == self.user:
                user_recommendations.append(referral)
        return user_recommendations


    def save (self, *args, **kwargs):
        if self.referral_code == "":
            code = generate_ref_code() 
            self.referral_code = code 
        super().save(*args, **kwargs)