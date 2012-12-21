from django.conf.urls.defaults import *
from good_beer.bad_movie.views import *
from good_beer.bad_movie.movie import *
from good_beer.bad_movie.beer import *
from good_beer.bad_movie.user_views import *


urlpatterns = patterns('good_beer.bad_movie.gbbm_views.index',
    url(r'^$', index),
    url(r'^add-movie/$', addMovie),
    url(r'^add-beer/$', addBeer),
    url(r'^accounts/register/$', registerUser),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'myapp/login.html'}),
)
