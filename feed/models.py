from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    done = models.BooleanField(default=False, blank=True)


    def __str__(self):
        return self.text
    