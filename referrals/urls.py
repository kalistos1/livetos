from django.urls import path
from . import views 

urlpatterns = [
    path('', views.referals , name ="referals"),
    path('<str:ref_code>/',views.referals , name ="referals"),
]