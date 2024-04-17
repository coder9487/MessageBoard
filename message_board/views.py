from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
import logging

@login_required
def message_board(request):
    current_user = request.user.username
    print("Current User: ", current_user)
    return render(request, "message_board.html" )
