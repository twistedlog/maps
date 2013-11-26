from django.db import models


class Locations(models.Model):

    """ Master Table for locations with (long, lat)."""

    name = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __unicode__(self):
        return u"{0} ({1}, {2})".format(
            self.name, self.longitude, self.latitude
        )


class Path(models.Model):

    """Path model contains master list of Paths."""
    PERM_GROUPS = (
        ('ADMIN', 'ADMIN'),
        ('STAFF', 'STAFF'),
        ('NORMAL', 'NORMAL'),
    )

    COLOR_CODES = (
        ('#FF0000', 'red'),
        ('#00FF00', 'green'),
        ('#0000FF', 'blue'),
    )

    src = models.ForeignKey(Locations, related_name='path_src')
    dest = models.ForeignKey(Locations, related_name='path_dest')
    group = models.CharField(max_length=10, choices=PERM_GROUPS)
    color = models.CharField(max_length=8, choices=COLOR_CODES)

    def __unicode__(self):
        return u"{0} -> {1}".format(
            self.src, self.dest
        )


class Routes(models.Model):

    """Contains all the hops in bw a path."""

    src = models.ForeignKey(Locations, related_name='route_src')
    dest = models.ForeignKey(Locations, related_name='route_dest')
    path = models.ForeignKey(Path)
    priority = models.IntegerField()

    def __unicode__(self):
        return u"{0} ->{1}  priority: {2}".format(
            self.src, self.dest, self.priority
        )


class RouteDetail(models.Model):
    route = models.ForeignKey(Routes)
    longitude = models.FloatField()
    latitude = models.FloatField()
    priority = models.IntegerField()

    def __unicode__(self):
        return u"({0},{1}) priority: {2} route: {3} path: {4}".format(
            self.longitude, self.latitude, self.priority, self.route.id,
            self.route.path.id
        )
