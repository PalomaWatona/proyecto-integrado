from django.contrib import admin
from django.urls import path
from ficha import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('menuA/', views.menu),
    path('menuB/', views.menu),
    path('login/', views.iniciarSesion),
    path('logout/', views.cerrarSesion),
]
