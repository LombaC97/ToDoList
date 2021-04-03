#Import all the needed modules
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Folder, Activity
# Create your views here.

#Login mixin to check if user is already logged in
#Function display folders, this will render all the available folders to the user and manage a new folder creation
@login_required
def display_folders(request):
 
    if request.POST:
        if request.POST.get('new_folder') != "":
            new = Folder(name=request.POST.get('new_folder'), user_id = request.user)
            new.save()
    folders = Folder.objects.filter(user_id = request.user)
  
    return render(request, 'folders_atoms/base.html', {"folders": folders, "username": request.user.username})

#Function delete folder
@login_required
def delete_folder(request):
    try:
        if request.POST.get('delete_id'):
            folder = Folder.objects.get(folder_id = request.POST['delete_id'])
            if folder.user_id.id == request.user.id:
                folder.delete()
    except:
        pass
    return HttpResponse('')

#Function to display all the activities in a folder. 
@login_required
def display_activities(request, pk = None):
    #If there's an error trying to get the folder, it means that the user doesn't have permission to see that folder
    #Or directly that the folder exists. In both cases, user will be redirected to folders view
    try:
        folder = Folder.objects.get(pk = pk, user_id = request.user)
    except:
        return redirect(reverse_lazy('folders'))
    #Manage if a new activity is created
    if request.POST:        
        if request.POST.get('new_activity') != "":
            new = Activity(name=request.POST['new_activity'], folder_id = folder)
            new.save()
    #Fetch all activities
    activities = Activity.objects.filter(folder_id = pk, folder_id__user_id = request.user)

    return render(request, 'folders_atoms/activities.html', {"activities": activities, "folder_id": pk,"folder_name": folder.name, "username": request.user.username})

#Function to delete activity
@login_required
def delete_activity(request):
    
    if request.POST.get('delete_id'):
        #We try to get the activity, if there's an error, it means that the activity doesn't belong to this user or folder
        try:
            activity = Activity.objects.get(pk = request.POST['delete_id'],folder_id=request.POST['folder_id'] ,folder_id__user_id = request.user)
            activity.delete()
        except:
            pass
    
    return HttpResponse('')

#Function to edit activities
@login_required
def edit_activity(request, pk):
    try:
        activity = Activity.objects.get(pk = pk, folder_id__user_id = request.user)
       
        if request.POST:
            if request.POST.get('edit_name'):
                activity.name = request.POST['edit_name']
                activity.save()
                return redirect(reverse_lazy('activities', kwargs={'pk': activity.folder_id.folder_id}))
    except:
        return redirect(reverse_lazy('folders'))
    
    return render(request, 'folders_atoms/edit_activity.html', {"activity": activity})

