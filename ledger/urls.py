from django.urls import path
from .views import index, recipes_list#every new page gets added here
urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipes_list, name='recipes_list'),
]

app_name = "ledger"
