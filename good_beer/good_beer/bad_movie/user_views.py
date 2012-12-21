from django.template import loader, RequestContext
from django.http import HttpResponse
from good_beer.bad_movie import models
from good_beer.bad_movie.forms import *
from django import forms
import datetime

def registerUser(request):
    regForm = RegForm
    if request.method == 'POST':
        regForm = RegForm(request.POST)
        if regForm.is_valid:
            regForm.save()
            
            
    t=loader.get_template('user/register.html')
    c = RequestContext(request, {'regForm':regForm})
    return HttpResponse(t.render(c))
