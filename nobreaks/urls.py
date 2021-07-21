from django.urls import path
from .views import nobreaks_list
from .views import nobreaks_new
from .views import nobreaks_update
from .views import nobreaks_delete

urlpatterns = [
    path('list/', nobreaks_list, name="nobreaks_list"),
    path('new/', nobreaks_new, name="nobreaks_new"),
    path('update/<int:id>', nobreaks_update, name="nobreaks_update"),
    path('delete/<int:id>', nobreaks_delete, name="nobreaks_delete"),

]