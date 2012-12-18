from django.contrib import admin
from good_beer.bad_movie import models

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    
class BeerAdmin(admin.ModelAdmin):
    list_display = ['label', 'style', 'brewery', 'rating']
    
class StyleAdmin(admin.ModelAdmin):
    list_display = ['style', 'notes']

class BreweryAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year']
    
class GenreAdmin(admin.ModelAdmin):
    list_display = ['movie', 'genre']
    
admin.site.register(models.User, UserAdmin)    
admin.site.register(models.Beer, BeerAdmin)
admin.site.register(models.Style, StyleAdmin)
admin.site.register(models.Brewery, BreweryAdmin)
admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Genre, GenreAdmin)