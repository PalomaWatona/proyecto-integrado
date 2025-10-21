from django.contrib import admin
from django.urls import path
from datosMedicos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('inicio/', views.menu_default, name='menu'),
    path('formulario/', views.formulario, name='formulario'),
    path('procesado/', views.procesado, name='procesado'),
    path('logout/', views.logout_view, name='logout'),
    
]

