from django.db import models


class Cities(models.Model):
    """ Master Table for cities with (long, lat)"""
    city = models.CharField(max_length=200)
    longitude = models.IntField()
    latitude = models.IntField()


class Path(models.Model):
    """Path model contains master list of Paths"""
    src = models.ForeignKey(Cities)
    dest = models.ForeignKey(Cities)


class Routes(models.Model):
    """Contains all the hops in bw a path"""
    src = models.ForeignKey(Cities)
    dest = models.ForeignKey(Cities)
    path = models.ForeignKey(Path)
    priority = models.IntField()
