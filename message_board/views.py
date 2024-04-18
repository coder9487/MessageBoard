from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from . import models
from datetime import datetime,timezone

@login_required
def message_board(request):
    current_user = request.user.username
    print("Current User: ", current_user)

    #  Check if the user has an avatar image
    fs = FileSystemStorage()
    user_avatar_image_url_base = 'message_board'
    user_avatar_image_url = '/static/USER_DATA/'+current_user+'/avatar.png'

    if fs.exists(user_avatar_image_url_base+user_avatar_image_url):
        print("User Avatar Image URL Exists ")
        user_avatar_image_url = user_avatar_image_url
    else:
        user_avatar_image_url = '/static/default_avatar.png'
        print("User Avatar Image URL Does Not Exist ")
    print("User Avatar Image URL: ", user_avatar_image_url)






    if request.method == "POST":
        print("POST Request: ", request.POST)
        print("POST Request: ", request.POST['message'])
        print("Current User to send  ", current_user)
        # Get the current UTC time
        current_utc_time = str(datetime.now(timezone.utc))

        # Create a new post with the current UTC time
        post = models.Post(username=current_user, message=request.POST['message'], timestemp=current_utc_time)
        post.save()


    return render(request, "message_board.html" ,
                  {'user_avatar_image_url': user_avatar_image_url,
                   'username': current_user,
                   'message_board': models.Post.objects.all()
                   }
                  )
