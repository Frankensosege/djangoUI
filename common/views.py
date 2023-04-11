from django.shortcuts import render, redirect

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form':form})


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


# from django.template import loader
# def exam1(request):
#     template = loader.get_template('exam1.html')
#     # print(template)
#     return HttpResponse(template.render(None, request))

# def exam2(request):
#     template = loader.get_template('exam2.html')
#     context = {'name': 'test', 'address':'서울시'}
#     return HttpResponse(template.render(context, request))
#     # == return render(request, 'exam2.html', context)