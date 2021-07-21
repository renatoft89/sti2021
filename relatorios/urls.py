from django.urls import path
from .views import rel_equipamentos

urlpatterns = [
    path('rel_pcs/', rel_equipamentos, name="relatorios"),
    
]