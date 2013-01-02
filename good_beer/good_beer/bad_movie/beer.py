from django.template import loader, Context
from django.http import HttpResponse


def addBeer(request):
    return HttpResponse("adding beer")