from django.urls import path
from .views import usuarios_list
from .views import usuarios_new
from .views import usuario_update
from .views import usuario_delete

urlpatterns = [
    path('list/', usuarios_list, name="usuarios_list"),
    path('new/', usuarios_new, name="usuarios_new"),
    path('update/<int:id>', usuario_update, name="usuario_update"),
    path('delete/<int:id>', usuario_delete, name="usuario_delete"),
    
]