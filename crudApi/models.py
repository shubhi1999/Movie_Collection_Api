from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Movie(models.Model):

    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=255, default='')
    genres = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.uuid.__str__()

    def __iter__(self):
        return iter([ self.uuid, 
                 self.title, 
                 self.description, 
                 self.genres, 
                 ]) 

class Collection(models.Model):
    
    collection_uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=255, default='')
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies', db_index=True,)
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)

    def __str__(self):
        return self.collection_uuid.__str__()