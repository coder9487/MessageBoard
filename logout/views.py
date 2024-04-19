from django.shortcuts import render
from django.contrib.auth import logout


def logout_view(request):
    print("Logout View")
    logout(request)
    return render(request, 'logout.html')