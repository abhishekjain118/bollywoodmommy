from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    violence_scale = models.IntegerField(default=5)
    horror_scale = models.IntegerField(default=5)
    blood_scale = models.IntegerField(default=5)
    alcohol_drugs_scale = models.IntegerField(default=5)
    abusive_language_scale = models.IntegerField(default=5)
    sex_nudity_scale = models.IntegerField(default=5)
    sensetive_religious_scale = models.IntegerField(default=5)
    racism_scale = models.IntegerField(default=5)
    overall_child_friendliness_scale = models.IntegerField(default=5)
    user_comments = models.CharField(max_length=2000, default='Something else which can bother children?')
    def __str__(self):
        return self.movie_title

