from django.db import models

# Create your models here.

class Subscription(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    currency = models.CharField(max_length=250)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def ___str___(self):
        return self.name
