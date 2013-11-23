from django.db import models


class Cities(models.Model):
    """ Master Table for cities with (long, lat)"""
    city = models.CharField(max_length=200)
    longitude = models.IntegerField()
    latitude = models.IntegerField()


class Path(models.Model):
    """Path model contains master list of Paths"""
    src = models.ForeignKey(Cities, related_name='path_src')
    dest = models.ForeignKey(Cities, related_name='path_dext')


class Routes(models.Model):
    """Contains all the hops in bw a path"""
    src = models.ForeignKey(Cities, related_name='route_src')
    dest = models.ForeignKey(Cities, related_name='route_dest')
    path = models.ForeignKey(Path)
    priority = models.IntegerField()
