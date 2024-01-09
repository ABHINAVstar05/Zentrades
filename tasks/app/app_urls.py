from django.urls import path
from .views import *

urlpatterns = [
    path('fetch_json/', fetch_json),
    path('json_data_api/', json_data),
    path('show_json_data/', show_json_data),    
]