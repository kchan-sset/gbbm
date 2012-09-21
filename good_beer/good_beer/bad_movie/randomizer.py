from good_beer.bad_movie.models import Beer, Movie
import random

class Randomizer:
    METHOD_MAX = 3
    METHOD_RATE = 3
    TRACKING_MAX = 10
    TYPE_DEFAULT = 'default'
    TYPE_FORCED = 'forced'
    TYPE_1 = 'Country'
    TYPE_2 = 'Terms'
    TYPE_3 = 'Featured'
    
    beerModel = ''
    movieModel = ''
    rType = ''
    nfData = ''
    beerObj = ''
    movieObj = ''
    
    def __init__(self):
        self.beerModel = Beer
        self.movieModel = Movie
        
    def pickOne():
        methodName = 'method'
        defaultTest = random.randint(1, self.METHOD_RATE)
        
        if defaultTest == self.METHOD_RATE:
            methodType = random.randint(1, self.METHOD_RATE)
        else:
            methodType = 'Default'
            
        methodName =+ methodType 
        getattr(self, methodName)
        
    def methodDefault(self):
        beerList = list(self.beerModel.objects.all())
        movieList = list(self.movieModel.objects.all())
        
        random.shuffle(beerList)
        random.shuffle(movieList)
            
        self.beerObj = beerList[0]
        self.movieObj = movieList[0]
        
        return self
    
    def method1(self):
        pass
    
    def method2(self):
        pass
    
    def method3(self):
        pass