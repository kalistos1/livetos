from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Testimoney(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    customer_name = models.CharField( max_length = 100, blank = True, null = True)
    customer_title = models.CharField(max_length = 100, blank = False, null = True)
    customer_photo = models.ImageField(blank = True, upload_to='testimoney/' )
    testimoney = models.TextField(blank = True, null = True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name

