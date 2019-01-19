from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from userauth import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('admin/', admin.site.urls),


]