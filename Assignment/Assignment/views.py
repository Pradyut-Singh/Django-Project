from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'project.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def service(request):
    return render(request, 'services.html')