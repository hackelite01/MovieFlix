from django.db import models
from django.utils.safestring import mark_safe

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class Country(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define the primary key
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

class State(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define the primary key
    country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='country_id')
    state_name = models.CharField(max_length=100)

    def __str__(self):
        return self.state_name

class City(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define the primary key
    state = models.ForeignKey(State, on_delete=models.CASCADE, db_column='state_id')
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name

class Actor(models.Model):
    # MALE = 'Male'
    # FEMALE = 'Female'
    # GENDER_CHOICES = [
    #     (MALE, 'Male'),
    #     (FEMALE, 'Female'),
    # ]

    id = models.AutoField(primary_key=True)  # Explicitly define the primary key
    a_country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='a_country')
    a_state = models.ForeignKey(State, on_delete=models.CASCADE, db_column='a_state')
    a_city = models.ForeignKey(City, on_delete=models.CASCADE, db_column='a_city')
    a_name = models.CharField(max_length=100)
    a_pic = models.ImageField(upload_to='actors/')
    a_bio = models.TextField()
    a_nationality = models.CharField(max_length=100)
    a_awards = models.CharField(max_length=100)
    a_gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    a_birthdate = models.DateField()

    def __str__(self):
        return self.a_name
    
    def actor_photo(self):
        if self.a_pic:
            return mark_safe('<img src="{}" width="100"/>'.format(self.a_pic.url))
        return '-'
    actor_photo.short_description = 'Actor'
    
class User(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define the primary key
    
    u_country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='u_country')
    u_state = models.ForeignKey(State, on_delete=models.CASCADE, db_column='u_state')
    u_city = models.ForeignKey(City, on_delete=models.CASCADE, db_column='u_city')
    u_name = models.CharField(max_length=100)
    u_dp = models.ImageField(upload_to='users/')
    u_gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    u_email = models.EmailField()
    u_phone = models.CharField(max_length=15)
    STATUS_CHOICES = [
        (0, 'Inactive'),
        (1, 'Active')
    ]
    status = models.IntegerField(choices=STATUS_CHOICES)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.u_name
    
    def user_photo(self):
        if self.u_dp:
            return mark_safe('<img src="{}" width="100"/>'.format(self.u_dp.url))
        return '-'
    user_photo.short_description = 'User'

class Director(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define the primary key
    d_country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='d_country')
    d_state = models.ForeignKey(State, on_delete=models.CASCADE, db_column='d_state')
    d_city = models.ForeignKey(City, on_delete=models.CASCADE, db_column='d_city')
    d_name = models.CharField(max_length=100)
    d_pic = models.ImageField(upload_to='directors/')
    d_bio = models.TextField()
    nationality = models.CharField(max_length=100)
    awards = models.TextField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    def __str__(self):
        return self.d_name
    
    def director_photo(self):
        if self.d_pic:
            return mark_safe('<img src="{}" width="100"/>'.format(self.d_pic.url))
        return '-'
    director_photo.short_description = 'Director'

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    # directors = models.ManyToManyField(Director)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='posters/')
    trailer = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def poster_photo(self):
        if self.poster:
            return mark_safe('<img src="{}" width="100"/>'.format(self.poster.url))
        return '-'
    poster_photo.short_description = 'Poster'


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.movie.title} by {self.user.u_name}'

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.u_name} - {self.movie.title}'
