from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.utils import timezone
from .models import Users
from .forms import UsersForm

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
            request.session['login_id'] = user.id
            # redirect_to = reverse('login:welcome', kwargs={'name':user.user_name})
            return redirect('login:welcome', {'user':user})
            # return HttpResponseRedirect(redirect_to)
        else:
            # display an error message
            error = 'Invalid credentials. Please try again.'

    # render the login page
    return render(request, 'login/main.html', {'error' : error})

def home(request, name):
    error = None
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print('name : ', name)

    return render(request, 'login/home.html', {'name':name})

def register(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.create_date = timezone.now()
            user.lastupdate_date = timezone.now()
            user.save()
            return redirect('login:index')
    else:
        form = UsersForm()
    context = {'form':form}
    return render(request, 'login/register.html', context)