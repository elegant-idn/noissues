from django.urls import path
from onboarding.views import GetBoarding, CreateBoarding, CreateMock, GetMock, CreatePartner

urlpatterns = [
    path("createboarding/", CreateBoarding.as_view(), name = "create_boarding" ),
    path("getboarding/", GetBoarding.as_view(), name = "get_boarding"),
    path("createmock/", CreateMock.as_view(), name = "create_mock"),
    path("getmock/", GetMock.as_view(), name = "get_mock"),
    path("createpartner/", CreatePartner.as_view(), name = "create_partner")
]