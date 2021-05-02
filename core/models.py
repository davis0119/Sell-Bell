from django.db import models
from django.contrib.auth.models import User 

# Bells (services)
class Bell(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    price = models.FloatField(blank=True, default=0)
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(): # the Bell's associated user, the title and price
        return str(author.username) + "'s Bell: " + str(title) + ', $' + str(price)

# Rings (service requests)
class Ring(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    price = models.FloatField(blank=True, default=0)
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(): # the Ring's associated user, the title and price
        return str(author.username) + "'s Ring: " + str(title) + ', $' + str(price) 