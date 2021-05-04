from rest_framework import serializers
from .models import Movie, Collection


class CollectionSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)
    movies = serializers.ListField(required=True)

    class Meta:
        model = Collection
        fields = [ "title", "description", "movies" ]

# class MovieSerializer(serializers.ModelSerializer):
#     title = serializers.CharField(max_length=100)
#     description = serializers.CharField(max_length=255)
#     genres = serializers.CharField(max_length=100)
    
#     class Meta:
#         model = Movie
#         fields = '__all__'
        
