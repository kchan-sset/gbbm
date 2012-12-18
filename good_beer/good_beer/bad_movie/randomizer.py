from good_beer.bad_movie.models import Beer, Movie, FeaturedPair
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
        
    def pickOne(self):
        methodName = 'method'
        defaultTest = random.randint(1, self.METHOD_RATE)
        
        if defaultTest == self.METHOD_RATE:
            methodType = str(random.randint(1, self.METHOD_RATE))
        else:
            methodType = 'Default'
            
        methodName += methodType
        
        return getattr(self, methodName)()
    
    def getRandomModel(self, model):
        querySet = model.objects.all()
        return querySet.order_by('?')[0]
    
    def methodDefault(self):            
        self.beerObj = self.getRandomModel(Beer)
        self.movieObj = self.getRandomModel(Movie)
        
        return self 
    
    ##By Country
    def method1(self):
        from good_beer.bad_movie.models import Genre
        
        self.beerObj = self.getRandomModel(Beer)
        country = self.beerObj.brewery.country
        
        if country == 'US':
            genreQS = Genre.objects.exclude(genre__contains = 'Foreign')
        else:
            genreQS = Genre.objects.filter(genre__contains = 'Foreign')
                    
        self.movieObj = genreQS.order_by('?')[0].movie

        return self
    
    #By Keyword
    def method2(self):
        #used for OR sql equivalent stmts
        from django.db.models import Q
        import operator        
        
        cnt = 0;
        while (cnt < self.TRACKING_MAX):
            self.beerObj = self.getRandomModel(Beer)
            country = self.beerObj.brewery.country
            style = self.beerObj.style.style
            label = self.beerObj.label
            breweryName = self.beerObj.brewery.name
            
            movieQS = Movie.objects.filter(reduce(operator.or_, (Q(synopsis__contains=x) for x in [style, label, breweryName])))
            cnt += 1
            
            if movieQS.exists():
                break
                    
        if movieQS.exists():
            self.movieObj = movieQS.order_by('?')[0]   
            return self
        else:            
           return self.methodDefault()
    
    #By Featured Pair
    def method3(self):
        fPair = self.getRandomModel(FeaturedPair)
        self.beerObj = fPair.beer
        self.movieObj = fPair.movie
        
        print fPair.beer_id
        print fPair.movie_id
        return self
        