from django.template import loader, Context
from django.http import HttpResponse
from good_beer.bad_movie.randomizer import Randomizer
import random

def index(request):
    
    picker = Randomizer()
    results = picker.pickOne()
    t = loader.get_template('paired.html')
    c = Context({ 'beer':results.beerObj, 'movie':results.movieObj, 'user':request.user})
    
    return HttpResponse(t.render(c))