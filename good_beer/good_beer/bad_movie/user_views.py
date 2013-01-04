from django.template import loader, RequestContext
from django.http import HttpResponse
from good_beer.bad_movie import models
from good_beer.bad_movie.forms import *
from django import forms
from django.contrib.auth import authenticate, login


def registerUser(request):
    registration = regForm
    if request.method == 'POST':
        registration = regForm(request.POST)
        if registration.is_valid():
            # create a user            
            registration.save()
            
        
    t=loader.get_template('user/user_forms.html')
    c = RequestContext(request, {'formToUse':registration, 'form_title':'Create a New User'})
    return HttpResponse(t.render(c))

def logInUser(request):
    loginFormObj = loginForm
    if request.method == 'POST':
        userName = request.POST['username']
        pwd = request.POST['password']
        
        #fetching the User object
        user = authenticate(username=userName, password=pwd)
        
        if user is not None:
            if user.is_active:
                #setting up the session for the user
                login(request, user)
            else:
                #return a 'diabled account' message
                pass
        else:
            #return invalid creds message
            pass
        
    t=loader.get_template('user/user_forms.html')
    c = RequestContext(request, {'formToUse':loginFormObj, 'form_title':'Login'})
    return HttpResponse(t.render(c))
    