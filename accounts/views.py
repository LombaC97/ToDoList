
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.

#Used to register a new user
def sign_up_view(request):
    
    form = UserCreationForm()
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse_lazy('folders'))
        
    return render(request, 'registration/signup.html', {'form': form})

#Handler used to redirect a non existing url user request
def handler404(request, exception):
    return redirect(reverse_lazy('folders'))