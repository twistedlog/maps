from django.contrib import admin
from .models import Locations, Path, Routes, RouteDetail

admin.site.register(Locations)
admin.site.register(Path)
admin.site.register(Routes)
admin.site.register(RouteDetail)
