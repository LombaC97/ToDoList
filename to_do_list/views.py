from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Folder
# Create your views here.
@login_required
def display_folders(request):
  #  Folder.objects.all().delete()
    if request.POST:
        if request.POST.get('new_folder') != "":
            new = Folder(name=request.POST.get('new_folder'), user_id = request.user)
            new.save()
    folders = Folder.objects.filter(user_id = request.user)
    print(folders)
    return render(request, 'folders_atoms/base.html', {"folders": folders})

@login_required
def delete_folder(request):
    if request.POST.get('delete_id'):
        Folder.objects.filter(folder_id = request.POST['delete_id']).delete()

    return HttpResponse('')



