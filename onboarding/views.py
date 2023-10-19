from django.core import serializers
import json
from rest_framework import views, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from onboarding.models import Onboarding, Mock, Partner
from writers.views import message


# Create your views here
class CreateBoarding(views.APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        boarding = Onboarding(
            author = get_user_model().objects.get(pk = request.data.get("author")),
            desired_outcome = request.data.get("desired_outcome"),
            success_identity = request.data.get("success_identity"),
            success_matrics = request.data.get("success_matrics"),
            reward_options = request.data.get("reward_options"),
            reward = request.data.get("reward"),
            outcome_importance = request.data.get("outcome_importance"),
            outcome_period = request.data.get("outcome_period"),
            my_reason = request.data.get("my_reason"),
            held_back = request.data.get("problem"),
            trigger_detail = request.data.get("trigger_detail"),
            has_partner = request.data.get("has_partner"),
            is_sms = request.data.get("is_sms"),
            is_email = request.data.get("is_email"),
            is_push_notification = request.data.get("is_push_notification"),
        )
        boarding.save()
        return Response(data=boarding.id,status = status.HTTP_200_OK)

class CreatePartner(views.APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        for data in  json.loads(request.data.get("partners")):
            partner = Partner(
                board = Onboarding.objects.get(pk = request.data.get("board_id")),
                email = data['email'],
                access_level = data['access_level']
            )
            partner.save()
        return Response(status=status.HTTP_200_OK)


class GetBoarding(views.APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        boarding = Onboarding.objects.get(author_id = request.data.get("author"))
        partners = Partner.objects.filter(board_id = boarding.id)
        response_data = {
            "boarding" : serializers.serialize('json', [boarding])[1:-1],
            "partners" : json.dumps(list(partners.values())),
        }
        return Response(data=response_data, status=status.HTTP_200_OK)

class CreateMock(views.APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        mock = Mock(
            category = request.data.get("category"),
            choice = request.data.get("choice")
        )
        mock.save()
        return Response(status = status.HTTP_200_OK)

class GetMock(views.APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        categories = Mock.objects.filter(category = "area")
        in_app_options = Mock.objects.filter(category = "in_app_options")
        rewards_options = Mock.objects.filter(category = "rewards_options")
        problems = Mock.objects.filter(category = "problems")
        videos = Mock.objects.filter(category = "videos")
        response_data = {
            "categories" : json.dumps(list(categories.values())),
            "in_app_options" : json.dumps(list(in_app_options.values())),
            "rewards_options" : json.dumps(list(rewards_options.values())),
            "problems" : json.dumps(list(problems.values())),
            "videos" : json.dumps(list(videos.values()))
        }
        return Response(data=response_data, status=status.HTTP_200_OK)