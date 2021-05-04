from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

#Logins
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # this is essentially hashing password to go into your settings.py file and it sets it as the hash.
            user.set_password(user.password)
            user.save()

            """And I'm going to say profile_form.save() but here is one point to passen (commit =false).I don't want to commit to the database yet.
            Otherwise I may get errors with collisions where it tries to overwrite this user(line17:user = user_form.save()).
            So we're going to do instead is say *profile.user = user* and that sets up that OneToOne relationship.
            So if you come back to models remember over here the user profile info that user is equal to a one toone relationship with the user here.
            So this one to one relationship is defined in the views with this line of code *profile.user= user* which is the user_form 
            which you come back here is this original form(form.py)UserForm class META model= user"""
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request,'basic_app/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username ,password =password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('basic_app:index'))
            else:
                return HttpResponse("Account Not ACTIVE!!")
        else:
            print("Username {} and password {}".format(username,password))
            return HttpResponse("Invalid Login")
    else:
        return render(request,'basic_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basic_app:index'))

