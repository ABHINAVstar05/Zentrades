from django.urls import path
from .views import *

urlpatterns = [
    path('fetch_json/', fetch_json),
    
]