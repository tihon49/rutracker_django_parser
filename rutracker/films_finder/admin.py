from django.contrib import admin

from films_finder.models import Film

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass