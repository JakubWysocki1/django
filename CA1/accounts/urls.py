from django.urls import path
from .views import SignUpView, ForgotPassword

urlpatterns = [
    path('password_reset', ForgotPassword.as_view(), name='password_reset'),
    path('signup/', SignUpView.as_view(), name='signup'),
]