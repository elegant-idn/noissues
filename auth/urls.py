from django.urls import path
from auth.views import SignInView, SignOutView, SignUpView, VerifyEmailView, VerifyCode, GetUsers, ForgotPassword
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="auth_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("verifycode/", VerifyCode.as_view(), name="verify_code"),
    path("forgotpassword/", ForgotPassword.as_view(), name="forgot_password"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signin/", SignInView.as_view(), name="signin"),
    path("signout/", SignOutView.as_view(), name="signout"),
    path("verifyemail/", VerifyEmailView.as_view(), name="verify_email"),
    path("getusers/", GetUsers.as_view(), name="get_users"),
]