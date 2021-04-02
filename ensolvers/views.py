from django.shortcuts import render_to_response, redirect
from django.urls import reverse_lazy
def handler404(request):
    return redirect(reverse_lazy('folders'))