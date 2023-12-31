import random
from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import  get_user_model, authenticate, login, logout
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.shortcuts import redirect
from django.conf import settings
from django.core import serializers
import json

from writers.serializers import WriterSerializer, SignupSerializer

# from auth.token import email_auth_token
from auth.utils import send_email

import jwt
# Create your views here.
class ChangePassword(views.APIView):
    def post(self, request, *arges, **kwargs):
        user = get_user_model().objects.get(email=request.data.get("email"))
        user.set_password(request.data.get("password"))
        user.save()
        return Response(status=status.HTTP_200_OK)
    
class UpdateProfile(views.APIView):
    def post(self, request, *args, **kwargs):
        user = get_user_model().objects.get(pk=request.data.get("pk"))
        user.first_name = request.data.get("first_name")
        user.last_name = request.data.get("last_name")
        user.name = request.data.get("name")
        user.email = request.data.get("email")
        user.save()
        return Response(data="The profile is updated.",status=status.HTTP_200_OK)
        
class GetUser(views.APIView):
    def post(self, request, *args, **kwargs):
        user = get_user_model().objects.get(pk=request.data.get("pk"))
        return Response(data=json.loads(serializers.serialize('json', [user]))[0]["fields"],status=status.HTTP_200_OK)

class VerifyCode(views.APIView):
    def post(self, request, *args, **kwargs):
        user = get_user_model().objects.get(pk=request.data.get("pk"))
        if user.verification_code == request.data.get("code"):
            user.is_email_verified = True
            user.save()
            return Response(data="The user is verified.",status=status.HTTP_200_OK)
        else:
            return Response(data="The verification code is not correct.",status=status.HTTP_401_UNAUTHORIZED)

class ForgotPassword(views.APIView):
    def post(self, request, *args, **kwargs):
        user = get_user_model().objects.get(email=request.data.get("email"))
        if user is not None:
            return Response(data=user.verification_code,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class SignUpView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.name = user.name.title()
            user.first_name = request.data.get("first_name")
            user.last_name = request.data.get("last_name")
            user.is_active = True
            verification_code = str(random.randint(100000, 999999))
            user.verification_code = verification_code
            user.save()

            # START: send email auth mail
            token = RefreshToken.for_user(user).access_token
            status_code = send_email(
                {
                    "email_subject": "Confirm your email",
                    "email_file": "mails/confirm_mail.html",
                    "email_data": {"verification_code": verification_code}
                },
                user,
                "Email auth"
            )
            return Response(data=user.pk,status=status_code)
            # END: send email auth mail

        return Response(
            data=serializer.errors, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
        )

class SignInView(views.APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        user = authenticate(
            username=data.get("email", None), password=data.get("password", None)
        )
        if user is not None:
            if user.is_email_verified:
                login(request, user)
                serializer = WriterSerializer(user)
                token = RefreshToken.for_user(user)
                result = serializer.data
                result["token"] = {
                    'refresh': str(token),
                    'access': str(token.access_token)
                }           
                return Response(status=status.HTTP_200_OK, data=result)
            return Response(
                status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                data={
                    "msg": "A verification mail is send to your email address. Please verify your email address to Login."
                },
            )
        return Response(data="The email or password is incorrect.",status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

class SignOutView(views.APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):
        refresh_token = request.data.get("refresh")
        token = RefreshToken(refresh_token)
        token.blacklist()

        user = get_user_model().objects.get(pk=request.data.get("pk"))
        logout(request)

        return Response(status=status.HTTP_200_OK)

class VerifyEmailView(views.APIView):
    def get(self, request, **kwargs):
        token = request.GET.get("token")
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = get_user_model().objects.get(pk=payload["user_pk"])
        except (jwt.exceptions.InvalidSignatureError, get_user_model().DoesNotExist):
            user = None
        if user is not None:
            user.is_email_verified = True
            user.save()
            link = f"{settings.CLIENT_URL}/emailconfirmation/success/{user.pk}/"
            return redirect(link)
        link = f"{settings.CLIENT_URL}/emailconfirmation/failure/"
        return redirect(link)
