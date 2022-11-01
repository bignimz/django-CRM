from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('leads/', leads_list, name="leads"),
    path('leads/<int:pk>/', lead_detail),
    path('leads/create/', lead_create, name="create"),
]
