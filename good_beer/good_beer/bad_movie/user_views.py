from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from good_beer.bad_movie import models
from good_beer.bad_movie.forms import *
from django.contrib.auth import authenticate, login, logout


def gbbm_register(request):
    registration = RegForm
    if request.method == 'POST':
        registration = regForm(request.POST)
        if registration.is_valid():
            # create a user            
            registration.save()
            
        
    t=loader.get_template('user/register.html')
    c = RequestContext(request, {'regForm':registration})
    return HttpResponse(t.render(c))

def gbbm_login(request):
    errMsg = None
    user = None
    referer = request.META['HTTP_REFERER']

    loginFormObj = LoginForm
    if request.method == 'POST':
        userName = request.POST['username']
        pwd = request.POST['password']
        
        #fetching the User object
        user = authenticate(username=userName, password=pwd)

        if user is not None:
            if user.is_active:
                #setting up the session for the user
                login(request, user)
                return HttpResponseRedirect(request.POST['referer'])
            else:
                #return a 'diabled account' message
                errMsg = "User is not active."
        else:
            #return invalid creds message
            errMsg = "There is no user that matches those credentials."
    
    if errMsg is not None:
        return HttpResponse(errMsg)
        
    
    t=loader.get_template('user/login.html')
    c = RequestContext(
        request,
        {'formToUse':loginFormObj,
         'form_title':'Login',
         'referer':referer})
    return HttpResponse(t.render(c))
    
def gbbm_logout(request):
    logout(request)
    return HttpResponseRedirect("/")