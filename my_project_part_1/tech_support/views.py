# Задание 1. tech support.py

from django.http import JsonResponse
from tech_support.models import Statistic


def statistics(request):
    statistic_list = Statistic.objects.all()
    result = []
    for statistic in statistic_list:
        result.append({
            'id': statistic.id,
            'author': statistic.author,
            'day': statistic.day,
            'store': statistic.store,
            'reason': statistic.reason,
            'status': statistic.status,
            'timestamp': statistic.timestamp,
        })

    return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})
