from django.contrib import admin
from .models import Genre, Movie, NowShowingMovie, Review, Comment
# Register your models here.

admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(Movie)
admin.site.register(NowShowingMovie)
admin.site.register(Review)
