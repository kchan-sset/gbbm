from django.template import loader, RequestContext
from django.http import HttpResponse
from good_beer.bad_movie import models
import datetime


def addMovie(request):
    movieForm = models.MovieForm
    if request.method == 'POST':
        movieForm = models.MovieForm(request.POST)
        if movieForm.is_valid():
            now = datetime.datetime.now()
            movieObj = movieForm.save(commit=False)
            movieObj.created_at = now.strftime("%Y-%m-%d %H:%M:%S")
            movieObj.save()
            
            return HttpResponse("Movie added")
            
    t=loader.get_template('add_movie.html')
    c = RequestContext(request, {'movieForm':movieForm})
    return HttpResponse(t.render(c))
    