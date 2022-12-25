from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify
from accounts.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=30, blank = False, null = False)
    email = models.EmailField()
    subject = models.CharField(max_length=300,blank = False, null = False)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True,)
    date_created = models.DateTimeField(max_length=100,auto_now_add=True)

    def __str__(self):
        return self.subject
    
    def save(self, *args, **kwargs):        
        value =str(self.subject) + str(self.name)
        self.slug = slugify(value, allow_unicode=True)
        super(ContactMessage, self).save(*args, **kwargs)
        
    def get_snippet (self):
        return self.body[:50 ] +"" +"......"