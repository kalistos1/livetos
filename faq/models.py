from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Faq(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField( max_length = 100, blank = False, null = False)
    question = models.TextField(blank = False, null = False)
    answer = models.TextField(blank = False, null = False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name, self.user.email

