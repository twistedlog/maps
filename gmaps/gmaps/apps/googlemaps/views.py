from django.shortcuts import render
from django.views.generic.base import View
from .models import Path

# Create your views here.

class RoutesView(View):
    http_method_names = ['get']

    def get(self, request):
        paths = Path.objects.all()
        return render(request, 'layout.html', {'paths': paths})


class RouteView(View):
    http_method_names = ['post']

    def post(self, request, id):
        pass