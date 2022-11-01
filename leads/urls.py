from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('leads/', leads_list, name="leads"),
    path('leads/<pk>/', lead_detail),
]
