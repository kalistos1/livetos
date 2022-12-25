from django.urls import path
from .import views

app_name ="testimoney"

urlpatterns = [ 
   path('all_testimonial',views.all_testimoney, name ="all_testimoney"),
   path('add_testimnial',views.create_testimoney, name ="create_testimoney"),
   path('update_testimonial/<int:id>',views.update_testimoney, name ="update_testimoney"),
   path('delete_testimonial/<int:id>',views.delete_testimoney, name ="delete_testimoney"),
]