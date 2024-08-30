from django.urls import path
from .views import AdModify , AdDetail

urlpatterns = [
    path("AdDetail/<int:pk>" , AdDetail.as_view()),
    path("AdModify" , AdModify.as_view())
]