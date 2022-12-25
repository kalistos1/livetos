from django.contrib import admin
from django.urls import path, include, re_path as url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.views.static import serve


urlpatterns = [
    path('', include("core.urls")),
    path('accounts/', include("accounts.urls")),
    path('blog/', include("blog.urls")),
    path('dashboard/', include("dashboard.urls")),
    path('dashboard/', include("faq.urls")),
    path('admin/', admin.site.urls),
    path('referrals/', include("referrals.urls")),
   
]


if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
