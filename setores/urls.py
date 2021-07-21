from django.urls import path
from .views import setores_list
from .views import setores_new
from .views import setores_update
from .views import setores_delete

urlpatterns = [
    path('list/', setores_list, name="setores_list"),
    path('new/', setores_new, name="setores_new"),
    path('update/<int:id>', setores_update, name="setores_update"),
    path('delete/<int:id>', setores_delete, name="setores_delete"),
]
