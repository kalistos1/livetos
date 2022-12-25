from django.urls import path

from . import views


app_name = "dashboard"

urlpatterns =[
    path('<str:username>/', views.dashboard_analytics, name = "analytics"),
    path('profile/<str:username>/', views.profile, name = "profile"),
    ]