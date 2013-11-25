from django.shortcuts import render
from django.views.generic.base import View
from .models import Path, Routes, RouteDetail
from django.http import HttpResponse
import json

# Create your views here.


class PathView(View):

    """PathView."""

    http_method_names = ['get']

    def get(self, request):
        paths = Path.objects.all()
        return render(request, 'layout.html', {'paths': paths})


class RouteView(View):

    """RouteView."""

    http_method_names = ['post']

    def post(self, request, id):
        config = json.loads(request.body)
        if not config['config']['next']:
            # first time
            path = Path.objects.get(id=id)
            length = len(Routes.objects.filter(path=path))
            route = Routes.objects.filter(path=path)[0]
            next = route.id
            marker = [route.src.longitude, route.dest.latitude]
            coordinates = None

            return_config = {
                'length': length,
                'next': next,
                'marker': marker,
                'coordinates': coordinates,
            }
            return HttpResponse(json.dumps(return_config), content_type="application/json")
