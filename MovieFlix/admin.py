from django.contrib import admin
from .models import Country, State, City, Actor, User, Director, Genre, Movie, Review, Watchlist

# Define your custom admin classes
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_name']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['state_name', 'country']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name', 'state']

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['a_name','actor_photo', 'a_country', 'a_state', 'a_city', 'a_gender', 'a_birthdate']
    list_filter = ['a_country', 'a_state', 'a_city', 'a_gender']
    search_fields = ['a_name', 'a_bio', 'a_nationality']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['u_name','user_photo', 'u_country', 'u_state', 'u_city', 'u_gender', 'u_email', 'u_phone', 'status', 'date_joined']
    list_filter = ['u_country', 'u_state', 'u_city', 'u_gender', 'status']
    search_fields = ['u_name', 'u_email', 'u_phone']
    list_editable = ['status']
    list_per_page = 20

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['d_name','director_photo', 'd_country', 'd_state', 'd_city', 'gender']
    list_filter = ['d_country', 'd_state', 'd_city', 'gender']
    search_fields = ['d_name', 'd_bio', 'nationality', 'awards']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','poster_photo', 'director', 'release_year', 'genre']
    list_filter = ['director', 'release_year', 'genre']
    search_fields = ['title', 'description']
    filter_horizontal = ['actors']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'rating', 'created_at']
    list_filter = ['movie', 'user', 'rating']
    search_fields = ['movie__title', 'user__u_name']

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'added_at']
    list_filter = ['user', 'movie', 'added_at']
    search_fields = ['user__u_name', 'movie__title']
