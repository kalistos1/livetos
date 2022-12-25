from django.urls import path
from .import views


app_name ="faq"

urlpatterns = [ 
   path('admin/faq',views.all_faq, name ="all_faq"),
   path('admin/add_faq',views.create_faq, name ="create_faq"),
   path('admin/edit_faq/<int:id>',views.update_faq, name ="update_faq"),
   path('admin/delete_faq/<int:id>',views.delete_faq, name ="delete_faq"),
] 