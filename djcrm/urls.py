from django.contrib import admin
from django.urls import path, include

from leads.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('leads.urls')),
]
