# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from django.utils.encoding import smart_str
from django.db import models
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    token = models.CharField(max_length=96, blank=True)
    nftoken = models.CharField(max_length=255, blank=True)
    nfsecret = models.CharField(max_length=255, blank=True)
    nfauth = models.IntegerField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    activation_key = models.CharField(max_length=40)
    key_expires = models.DateTimeField()
    class Meta:
        db_table = u'user_profile'
    def __str__(self):
        #print out the username in the admin whenever there's a relationship in the admin
        return "%s" % (self.username)
    

#class User(models.Model):
#    id = models.BigIntegerField(primary_key=True)
#    username = models.CharField(max_length=255, unique=True)
#    password = models.CharField(max_length=255)
#    role = models.CharField(max_length=255)
#    email = models.CharField(max_length=255)
#    token = models.CharField(max_length=96, blank=True)
#    nftoken = models.CharField(max_length=255, blank=True)
#    nfsecret = models.CharField(max_length=255, blank=True)
#    nfauth = models.IntegerField()
#    created_at = models.DateTimeField(null=True, blank=True)
#    updated_at = models.DateTimeField(null=True, blank=True)
#    class Meta:
#        db_table = u'user'
#    def __str__(self):
#        #print out the username in the admin whenever there's a relationship in the admin
#        return "%s" % (self.username)

class Style(models.Model):
    id = models.BigIntegerField(primary_key=True)
    style = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    image = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'style'
    def __str__(self):
        return "%s" % (self.style)

class Brewery(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    image = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'brewery'
    def __str__(self):
        return "%s" % (smart_str(self.name))

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
        verbose_name = 'Beer Record'
        verbose_name_plural = 'Beers'

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
    def __str__(self):
        return "%s" % (self.title)

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
        
##FORM CREATION CLASSESS
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'rating', 'year', 'runtime', 'synopsis', 'image')
        widgets = {
            'synopsis': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        
#creating a signal/handle to create an associated user profile
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 