from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .forms import LoginForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
# Create your views here.
import re

print



def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)


        from_form_usermode = form.data['usermode']
        from_form_username = form.data['username']
        from_form_password = form.data['password']

        from_form_username = (re.sub('[^a-zA-Z]+', '', from_form_username))

        print("Username: ", from_form_username, "Password: ", from_form_password)
        
        if(from_form_usermode == 'signup'):
            print('signup')
            if signup_func(request,from_form_username,from_form_password) == 1:


                uploaded_file_url = ''


                myfile = request.FILES.get('user_imag_file', False)
                filetype = str(myfile).split('.')[-1]
                fs = FileSystemStorage()
                if filetype not in ['jpg','jpeg','png']:
                    uploaded_file_url = 'default_avatar.png'
                else:
                    filename = fs.save('message_board/static/USER_DATA/'+from_form_username+'/'+'avatar.'+filetype, myfile)
                    uploaded_file_url = fs.url(filename)
                
                print('uploaded_file_url:',uploaded_file_url)





                return render(request, 'login.html',status=400)
            else:
                return render(request, 'login.html',status=401)
        
        elif(from_form_usermode == 'login'):
            print('login')
            if login_func(request,from_form_username,from_form_password) == 1:
                #return render(request, 'login.html',status=400)
                return redirect('message_board/')
            else:
                return render(request, 'login.html',status=401)
        else:
            print('invalid')
            return render(request, 'login.html',status=401)
    else:
        form = LoginForm()
        return  render(request, "login.html", {"form": form, "messages": ""})



def login_func(request,from_form_username,from_form_password):
    user = authenticate(request, username=from_form_username, password=from_form_password)
    if user is not None:
        login(request, user)
        messages.success(request, 'User logged in successfully')
        print('User logged in successfully')
        return 1
    else:
        print('user not found')
        messages.error(request, 'Invalid username or password')
        print('Invalid username or password')
        return 0

def signup_func(request,from_form_username,from_form_password):
    # Check if the user already exists
    try:
        user = User.objects.get(username=from_form_username)
        messages.error(request, 'Username already exists')
        print('Username already exists')
        return 0
    except User.DoesNotExist:
        # If the user does not exist, create a new one
        user = User.objects.create_user(from_form_username, password=from_form_password)
        user.save()
        messages.success(request, 'User created successfully')
        print('User created successfully')
        return 1