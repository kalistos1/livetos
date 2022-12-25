from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
# Create your models here.
class User(AbstractUser):
    STATUS = (
        
        ('1', 'verified'),
        ('2', 'unverified'),
    )
    is_admin = models.BooleanField(default=False)
    t_and_c = models.BooleanField(default=False)
    email = models.CharField(max_length=350, unique=True)
    notification_enabled = models.BooleanField(default=True)
    account_status = models.CharField(max_length=3, default="2", choices=STATUS)
   

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'users'


    
class TempUrl(models.Model):
    url_hash = models.CharField("Url", blank=False, max_length=32, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    expires = models.DateTimeField("Expires")

    class Meta:
        db_table = "temp_urls"


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=30, null=True, blank=True)
    crypto_address = models.CharField(max_length=50,null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='users/', default='user.png',blank=True)       
    last_modified = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'profiles'


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
        
