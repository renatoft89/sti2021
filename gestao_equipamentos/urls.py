"""gestao_equipamentos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from equipamentos import urls as equipamentos_urls
from setores import urls as setores_urls
from nobreaks import urls as nobreaks_urls
from impressoras import urls as impressoras_urls
from usuarios import urls as usuarios_urls
from home import urls as home_urls
from relatorios import urls as relatorios_urls

'''from django.conf import settings
from django.urls.static import static'''
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('equipamentos/', include(equipamentos_urls)),
    path('setores/', include(setores_urls)),
    path('nobreaks/', include(nobreaks_urls)),
    path('impressoras/', include(impressoras_urls)),
    path('relatorios/', include(relatorios_urls)),
    path('usuarios/', include(usuarios_urls)),

    path('', include(home_urls)),
    path('admin/', admin.site.urls),
]
