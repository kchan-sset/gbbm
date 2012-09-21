from django.conf.urls.defaults import *
from good_beer.bad_movie.views import index

urlpatterns = patterns('',
    url(r'^$', index),
)