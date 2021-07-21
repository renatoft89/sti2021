from django.urls import path
from .views import maquinas_list
from .views import maquina_new
from .views import maquina_update
from .views import maquina_delete



urlpatterns = [
    path('list/', maquinas_list, name="maquinas_list"),
    path('new/', maquina_new, name="maquina_new"),
    path('update/<int:id>', maquina_update, name="maquina_update"),
    path('delete/<int:id>', maquina_delete, name="maquina_delete"),



]