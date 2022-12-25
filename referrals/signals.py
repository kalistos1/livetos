from .models import Referral
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_referals(sender, instance, created, *args, **kwargs):
    if created:
        Referral.objects.create(user=instance)


