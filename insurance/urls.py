from django.urls import path
from .views import register_user, get_tokens, PolicyListCreate, PolicyDetail, ClaimCreate

urlpatterns = [
    path('register/', register_user),
    path('token/', get_tokens),
    
    
    path('policies/', PolicyListCreate.as_view()),
    path('policies/<int:pk>', PolicyDetail.as_view()),
    path('claims/', ClaimCreate.as_view()),
]