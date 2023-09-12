from django.urls import path
from .views import *

app_name = "feed"

urlpatterns = [
    path('', Home, name="index")
]
