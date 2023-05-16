from cars.models import Car
from django.http import JsonResponse
from django.views import View
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404


# TODO ниже представлена функция, которую необходимо переписать на CBV 'CarView'
class CarView(DetailView):
    model = Car

    def get(self, request, *args, **kwargs):
        car = self.get_object()

        return JsonResponse({
            "id": car.pk,
            "slug": car.slug,
            "name": car.name,
            "brand": car.brand,
            "address": car.address,
            "description": car.description,
            "status": car.status,
            "created": car.created,
        })
