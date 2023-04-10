from django.shortcuts import render, redirect

def login_new(request):
    error = None
    if request.method == 'POST':
        usr_id = request.POST.get('useremail')
        pw = request.POST.get('password')
        # usr_id = request.form['id']
        # pw = request.form['pw']

        # query the database for the user with the given username and password
        # user = Users.objects.get(id=usr_id, passwd=pw)

        # if user is not None:
        #     # redirect the user to the home page
        #     request.session['login_id'] = user.id
        #     # redirect_to = reverse('login:welcome', kwargs={'name':user.user_name})
        #     return redirect('login:welcome', {'user': user})
        #     # return HttpResponseRedirect(redirect_to)
        # else:
        #     # display an error message
        #     error = 'Invalid credentials. Please try again.'

        return redirect('common:welcome', {'user': usr_id})

    # render the login page
    return render(request, 'common/login_new.html', {'error': error})

def signup_new(request):
    # if request.method == 'POST':
    #     form = UsersForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.create_date = timezone.now()
    #         user.lastupdate_date = timezone.now()
    #         user.save()
    #         return redirect('login:index')
    # else:
    #     form = UsersForm()
    # context = {'form':form}
    # return render(request, 'common/signup.html', context)
    return render(request, 'common/signup.html')