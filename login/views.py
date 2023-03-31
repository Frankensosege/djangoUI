from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users

# Create your views here.
def index(request):
    error = None
    if request.method == 'POST':
        usr_id = request.POST.get('id')
        pw = request.POST.get('pw')
        # usr_id = request.form['id']
        # pw = request.form['pw']

        # query the database for the user with the given username and password
        user = Users.objects.get(id=usr_id, passwd=pw)

        if user is not None:
            # redirect the user to the home page
            return redirect('login:welcome', name=user.user_name)
        else:
            # display an error message
            error = 'Invalid credentials. Please try again.'

    # render the login page
    return render(request, 'login/main.html', {'error' : error})

def home(request, name):
    error = None
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print(name)

    return render(request, 'login/home.html', name=name)

def register(request):
    print('==========================================')
    return render(request, 'login/register.html')