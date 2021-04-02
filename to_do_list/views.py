from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Folder, Activity
# Create your views here.
@login_required
def display_folders(request):
  #  Folder.objects.all().delete()
    if request.POST:
        if request.POST.get('new_folder') != "":
            new = Folder(name=request.POST.get('new_folder'), user_id = request.user)
            new.save()
    folders = Folder.objects.filter(user_id = request.user)
  
    return render(request, 'folders_atoms/base.html', {"folders": folders, "username": request.user.username})

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

@login_required
def display_activities(request, pk = None):
    try:
        folder = Folder.objects.get(pk = pk, user_id = request.user)
    except:
        return redirect(reverse_lazy('folders'))

    if request.POST:        
        if request.POST.get('new_activity') != "":
            new = Activity(name=request.POST['new_activity'], folder_id = folder)
            new.save()
    
    activities = Activity.objects.filter(folder_id = pk, folder_id__user_id = request.user)

    
    return render(request, 'folders_atoms/activities.html', {"activities": activities, "folder_id": pk,"folder_name": folder.name, "username": request.user.username})

@login_required
def delete_activity(request):
    
    if request.POST.get('delete_id'):
        try:
            activity = Activity.objects.get(pk = request.POST['delete_id'],folder_id=request.POST['folder_id'] ,folder_id__user_id = request.user)
            activity.delete()
        except:
            pass
    
    return HttpResponse('')

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

