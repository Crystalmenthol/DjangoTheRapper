from django.db import models
from artist.models import Artist

class Single(models.Model):
    artist= models.ForeignKey(Artist, to_field='id', on_delete=models.CASCADE, null=True)
    name= models.CharField(max_length=100)
    youtube_views= models.IntegerField()

    class Meta:
        db_table = 'single'