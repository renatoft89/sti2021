from django.urls import path
from .views import impressoras_list
from .views import impressoras_new
from .views import impressoras_update
from .views import impressoras_delete


urlpatterns = [
    path('list/', impressoras_list, name="impressoras_list"),
    path('new/', impressoras_new, name="impressoras_new"),
    path('update/<int:id>', impressoras_update, name="impressoras_update"),
    path('delete/<int:id>', impressoras_delete, name="impressoras_delete"),
]