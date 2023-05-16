from cars.models import Car
from django.http import JsonResponse


def get_car(request, pk):
    # TODO напишите view-функцию здесь (Readme.md, Задание get_car)
    try:
        result = Car.objects.get(id=pk)
    except:
        return JsonResponse({'Error': 'PK not found'}, status=404)
    return JsonResponse({
        'id': result.id,
        'slug': result.slug,
        'name': result.name,
        'brand': result.brand,
        'address': result.address,
        'description': result.description,
        'status': result.status,
        'created': result.created,
    })


def search(request):
    # TODO напишите view-функцию здесь (Readme.md, Задание car_search)
    brand = request.GET.get('brand', None)
    if brand:
        cars = Car.objects.all().filter(brand=brand)
        result = []
        for car in cars:
            result.append(
                {
                    'id': car.id,
                    'name': car.name,
                    'brand': car.brand,
                    'status': car.status,
                }
            )
        if result:
            return JsonResponse(result, safe=False)
        else:
            return JsonResponse({'Error': 'Brand not found'}, status=404)
    return JsonResponse({'Error': 'Empty request'}, status=404)
