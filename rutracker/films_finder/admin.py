from django.contrib import admin

from films_finder.models import Film

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'url']
    list_display_links = ['name', 'id', 'url']
    # list_filter = ['name']
    search_fields = ['name', 'description']