from django.urls import path, include

from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from rest_framework_jwt.views import refresh_jwt_token

from . import views


app_name = 'accounts'

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('check/email/', views.check_email),
    path('refresh/', refresh_jwt_token),
    path('music/like/', views.MusicView.as_view()),
    path('music/', views.my_music),
    path('tutorial/', views.TutorialView.as_view()),
    # path('likes_music/', views.likes_music),
    # path('like/', views.like),
]
