from django.shortcuts import render

def home (request):
    return render(request, 'home.html')
def start (request):
    return render(request, 'start.html')
