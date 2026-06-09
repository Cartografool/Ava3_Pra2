from django.contrib import admin
from django.urls import path
from formulario.views import receber_formulario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/formulario/', receber_formulario),
]