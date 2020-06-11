"""Prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from citas.views import Registro_Pediatras_View_Set, Generar_cita_View_Set

router = DefaultRouter()
router.register(r'citas', Generar_cita_View_Set, Registro_Pediatras_View_Set )


urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'Yema Test [César de León]'