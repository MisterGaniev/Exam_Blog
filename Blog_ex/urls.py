from django.contrib import admin
from django.urls import path
from app_1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login, name='login'),
    path('register/', Register, name='reg'),
    path('blog/', Blog.as_view(), name='blog'),
    path('logout/',   name='logout'),
]
