from django.urls import path
from . import views

app_name ="tickets"

urlpatterns = [
    path('create_ticket/', views.create_ticket, name = "create_ticket"),
    path('all_tickets/', views.all_tickets, name = "all_tickets"),
    path('read_ticket/<int:id>', views.delete_ticket, name = "read_ticket"),
    path('delete_ticket/<int:id>', views.read_ticket, name = "delete_ticket"),
]
