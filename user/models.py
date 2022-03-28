from django.db import models


class UserDetails(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
