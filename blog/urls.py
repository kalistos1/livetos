from django.urls import path
from . import views

app_name ="blog"

urlpatterns = [
    path('admin/blog_posts/', views.posts, name='blog_posts'),
    path('admin/single_post/<slug:slug>/', views.single_post, name='single_post'),
    path('admin/addpost/', views.admin_add_post, name='add_post'),
    path('admin/delete/<slug:slug>', views.admin_delete_post, name='delete_post'),
    path('admin/edit/<slug:slug>', views.admin_edit_post, name='edit_post'),
    path('admin/preview/<slug:slug>', views.single_post, name='preview_post'),
    path('', views.user_posts, name='user_all_post'),
    path('<slug:slug>/', views.user_single_post, name='user_single_post'),
    
]


#HTMX urls
htmx_urlpatterns = [
    path('add_comment/<slug:slug>/', views.add_comment, name="add_comment")
]

#concatenating both urls
urlpatterns += htmx_urlpatterns