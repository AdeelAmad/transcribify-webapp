from django.db import models

# Create your models here.
class customer(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    stripe_id = models.CharField(max_length=255, blank=True, null=True)