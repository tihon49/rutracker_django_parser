from rest_framework import serializers

from films_finder.models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'    # ['id', 'name', 'url']