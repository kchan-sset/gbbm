from django.conf.urls.defaults import *
from good_beer.bad_movie.views import *
from good_beer.bad_movie.movie import *
from good_beer.bad_movie.beer import *
from good_beer.bad_movie.user_views import *


urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^add-movie/$', addMovie),
    url(r'^add-beer/$', addBeer),
    url(r'^accounts/register/$', gbbm_register),
    url(r'^accounts/login/$', gbbm_login),
    url(r'^accounts/logout/$', gbbm_logout),
)
