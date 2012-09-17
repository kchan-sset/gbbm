# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=96, blank=True)
    nftoken = models.CharField(max_length=255, blank=True)
    nfsecret = models.CharField(max_length=255, blank=True)
    nfauth = models.IntegerField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'user'

class Style(models.Model):
    id = models.BigIntegerField(primary_key=True)
    style = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    image = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'style'

class Brewery(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    image = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'brewery'

class Beer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    author = models.ForeignKey(User, db_column='author')
    label = models.CharField(max_length=255)
    style = models.ForeignKey(Style, db_column='style')
    brewery = models.ForeignKey(Brewery, db_column='brewery')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    image = models.CharField(max_length=255, blank=True)
    rating = models.DecimalField(null=True, max_digits=20, decimal_places=1, blank=True)
    abv = models.CharField(max_length=255, blank=True)
    ibu = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'beer'

class Movie(models.Model):
    id = models.BigIntegerField(primary_key=True)
    author = models.ForeignKey(User, db_column='author')
    image = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    rating = models.DecimalField(null=True, max_digits=20, decimal_places=1, blank=True)
    year = models.IntegerField()
    nfid = models.CharField(max_length=255, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    synopsis = models.TextField(blank=True)
    nflink = models.CharField(max_length=255, blank=True)
    nfsimilar = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'movie'

class FeaturedPair(models.Model):
    id = models.BigIntegerField(primary_key=True)
    beer = models.ForeignKey(Beer)
    movie = models.ForeignKey(Movie)
    meta = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'featured_pair'

class Genre(models.Model):
    id = models.BigIntegerField(primary_key=True)
    movie = models.ForeignKey(Movie)
    genre = models.CharField(max_length=255)
    class Meta:
        db_table = u'genre'

class MigrationVersion(models.Model):
    version = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'migration_version'


class Session(models.Model):
    sess_id = models.CharField(max_length=255, primary_key=True)
    sess_data = models.TextField(blank=True)
    sess_time = models.IntegerField()
    class Meta:
        db_table = u'session'