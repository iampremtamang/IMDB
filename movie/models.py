from django.db import models

CATEGORY_CHOICES  = (
    ('action', 'ACTION'),
    ('drama', 'DRAMA'),
    ('comedy', 'COMEDY'),
    ('romance', 'ROMANCE')
)

LANGUAGE_CHOICES = (
    ('GR', 'GERMAN'),
    ('EN', 'ENGLISH')
)

STATUS_CHOICES = (
    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED')
)

class Movie(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField(max_length=1024)
    # tags = models.
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    cast = models.CharField(max_length=254)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)


    def __str__(self):
        return self.title

LINK_CHOICES = (
    ('D','DOWNLOAD'),
    ('W', 'WATCH')
)

class  MovieLink(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE) 
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField()

    def __str__(self):
        return self.movie.title