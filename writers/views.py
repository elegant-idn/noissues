from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model, authenticate, login, logout

from rest_framework import viewsets
from rest_framework import permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics, serializers, views, status
from rest_framework.response import Response
from django.shortcuts import redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.db.models import Q

# Email sending and auth requirements
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# Dev tools
from colorama import Fore, Style
import smtplib

from writers.serializers import (
    WriterSerializer,
    EmailUsernameSerializer,
    SearchWriterSerializer
)


def message(msg):
    print(Fore.MAGENTA, Style.BRIGHT, "\b\b[#]", Fore.RED, msg, Style.RESET_ALL)

class UsernameAndEmails(views.APIView):
    def get(self, request, **kwargs):
        serializer = EmailUsernameSerializer(get_user_model().objects.all(), many=True)
        return Response(status=200, data=serializer.data)

class SetupWriterAPI(views.APIView):
    def post(self, request, *args, **kwargs):
        user = get_user_model().objects.get(pk=kwargs["pk"])
        try:
            check = get_user_model().objects.get(username=request.data.get["username"])
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            check = None

        if check is not None:
            return Response(
                status = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                data = {"error": "Pen Name already taken"}
            )
        user.username = request.data.get("username")
        user.save()
        return Response(status = status.HTTP_200_OK)

class ManageWriterAPI(generics.RetrieveUpdateAPIView):    
    serializer_class = WriterSerializer
    queryset = get_user_model().objects.all()
    lookup_field = "pk"
    permission_classes = (IsAuthenticated, )

class DeleteWriterAPI(views.APIView):
    def post(self, request, *args, **kwargs):
        email = get_user_model().objects.get(pk=kwargs["pk"]).email
        password = request.data.get("password", None)
        user = authenticate(email = email, password = password)
        if user is not None:
            message(f"{user.name} ({user.pk}) deleted their account")
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


class SearchWriterAPI(views.APIView):
    def post(self, request, **kwargs):
        writer = request.data.get("username")
        bloggers = get_user_model().objects.filter(
            Q(username__contains=writer) | Q(name__contains=writer)
        )
        serializer = SearchWriterSerializer(bloggers, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
        
    def get(self, request, **kwargs):
        bloggers = get_user_model().objects.all()
        serializer = SearchWriterSerializer(bloggers, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)