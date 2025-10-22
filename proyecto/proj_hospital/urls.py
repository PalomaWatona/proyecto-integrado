from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from ficha import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.redir, name='redirect'),
    path('menu/', views.menu, name='menu'),
    path('login/', views.iniciarSesion),
    path('logout/', views.cerrarSesion),
]
