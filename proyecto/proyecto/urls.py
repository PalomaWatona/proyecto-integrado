from django.contrib import admin
from django.urls import path
from datosMedicos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.formulario02),
    #path('', views.login),
]
