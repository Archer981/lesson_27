from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView
from same_classes.models import Feedback, Destination
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
import json


@method_decorator(csrf_exempt, name='dispatch')
class FeedbackView(View):
    def get(self, request):
        feedbacks = Feedback.objects.all()
        response = []
        for feedback in feedbacks:
            response.append({
                "correlation_id": feedback.correlation_id,
                "user_feedback": feedback.user_feedback,
                "user_feedback_timestamp": feedback.user_feedback_timestamp,
                "closed": feedback.closed
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        feedback_data = json.loads(request.body)

        feedback = Feedback()
        feedback.user_feedback = feedback_data["user_feedback"]
        feedback.closed = feedback_data.get("closed", False)

        try:
            feedback.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        feedback.save()
        return JsonResponse({
            "id": feedback.id,
            "correlation_id": feedback.correlation_id,
        })


class FeedbackEntityView(View):
    def get(self, request, pk):
        feedback = get_object_or_404(Feedback, id=pk)

        return JsonResponse({
            "id": feedback.id,
            "correlation_id": feedback.correlation_id,
            "user_feedback": feedback.user_feedback,
            "user_feedback_timestamp": feedback.user_feedback_timestamp,
            "closed": feedback.closed
        })

# TODO ниже следует реализовать CBV для модели Destination
@method_decorator(csrf_exempt, name='dispatch')
class DestinationView(View):
    def get(self, request):
        result = []
        data = Destination.objects.all()
        for item in data:
            result.append({
                'id': item.id,
                'name': item.name,
            })
        return JsonResponse(result, safe=False)


    def post(self, request):
        destination_data = json.loads(request.body)
        destination = Destination()
        destination.name = destination_data.get('name', 'default_name')
        destination.to_name = destination_data.get('to_name', 'default_to_name')
        destination.flag = destination_data.get('flag', 'default_flag')
        destination.visa_id = destination_data.get('visa_id', 1)
        destination.covid_status = destination_data.get('covid_status', 1)

        try:
            destination.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)
        destination.save()
        return JsonResponse({
            'id': destination.id,
            'name': destination.name,
        }, safe=False)


class DestinationEntityView(View):
    def get(self, request, number):
        entity = get_object_or_404(Destination, pk=number)
        return JsonResponse({
            'id': entity.id,
            'name': entity.name,
            'to_name': entity.to_name,
            'flag': entity.flag,
            'visa_id': entity.visa_id,
            'covid_status': entity.covid_status,
        }, safe=False)


# TODO ниже следует реализовать generics(ListView, DetailView) CBV для модели Destination
class DestinationListView(ListView):
    model = Destination

    def get(self, request, **kwargs):
        super().get(request, **kwargs)
        result = []
        for item in self.object_list:
            result.append({
                'id': item.id,
                'name': item.name,
            })
        return JsonResponse(result, safe=False)


class DestinationDetailView(DetailView):
    model = Destination

    def get(self, request, **kwargs):
        super().get(request, **kwargs)
        self.object = self.get_object()
        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'visa_id': self.object.visa_id,
            'covid_status': self.object.covid_status,
        }, safe=False)
