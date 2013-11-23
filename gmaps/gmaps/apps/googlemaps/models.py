from django.db import models


class Locations(models.Model):
    """ Master Table for locations with (long, lat)"""
    name = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __unicode__(self):
        return u"{0} ({1}, {2})".format(
            self.name, self.longitude, self.latitude
        )

class Path(models.Model):
    """Path model contains master list of Paths"""
    src = models.ForeignKey(Locations, related_name='path_src')
    dest = models.ForeignKey(Locations, related_name='path_dest')

    def __unicode__(self):
        return u"{0} -> {1}".format(
            self.src, self.dest
        )


class Routes(models.Model):
    """Contains all the hops in bw a path"""
    src = models.ForeignKey(Locations, related_name='route_src')
    dest = models.ForeignKey(Locations, related_name='route_dest')
    path = models.ForeignKey(Path)
    priority = models.IntegerField()

    def __unicode__(self):
        return u"{0} ->{1}  priority: {2}".format(
            self.src, self.dest, self.priority
        )
