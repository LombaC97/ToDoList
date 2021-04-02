from django.urls import path
from .views import display_folders, delete_folder, display_activities, delete_activity, edit_activity


urlpatterns = [
    path('folders/', display_folders , name='folders'),
    path('folders/delete', delete_folder, name='delete_folder'),
    path('folders/<int:pk>/view', display_activities, name = 'activities'),
    path('folders/activities/delete', delete_activity , name = 'delete_activity'),
    path('folders/activities/<int:pk>/edit', edit_activity, name ='edit_activity')
]