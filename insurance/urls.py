from django.urls import path
from .views import register_user, get_tokens

urlpatterns = [
    path('register/', register_user),
    path('token/', get_tokens),
]