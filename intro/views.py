from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def intro(request):
    print("Intro Page")
    return render(request, 'intro.html')