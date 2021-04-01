from django.urls import path
from .views import display_folders, delete_folder


urlpatterns = [
    path('folders/', display_folders , name='folders'),
    path('folders/delete', delete_folder, name='delete_folder')
]