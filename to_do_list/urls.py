from django.urls import path
from .views import display_folders



urlpatterns = [
    path('folders/', display_folders , name='folders'),
]