from django.db import models
from django.contrib.auth.models import User 

# Bells (services)
class Bell(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    price = models.FloatField(blank=True, default=0)
    # image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(self): # the Bell's associated user, the title and price
        return str(self.author.username) + "'s Bell: " + str(self.title) + ', $' + str(self.price)
    def __add__(self, other):
        if other.isnumeric():
            self.price = self.price + other 
        return self.price

# Rings (service requests)
class Ring(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    price = models.FloatField(blank=True, default=0)
    # image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(self): # the Ring's associated user, the title and price
        return str(self.author.username) + "'s Ring: " + str(self.title) + ', $' + str(self.price) 
    def __add__(self, other):
        if other.isnumeric():
            self.price = self.price + other 
        return self.price

class Comment(models.Model):
    body = models.TextField()
    post_bell = models.ForeignKey(Bell, related_name="comments", on_delete=models.CASCADE, null=True, blank=True)
    post_ring = models.ForeignKey(Ring, related_name="comments", on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)