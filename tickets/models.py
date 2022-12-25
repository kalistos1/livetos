from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
from django.db import models

# Create your models here.




class TicketMessage(models.Model):
    title = models.CharField(max_length=100,)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(upload_to="tickets", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'ticket_messages'
        verbose_name = 'ticket message'
        verbose_name_plural = 'ticket messages'


    def __str__(self):
        return self.sender.get_fullname() + " " + str(self.id)




