from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views

# Serializers define the API representation.


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
path('reg_comp/', views.RegisterCompany.as_view()),
    path('fetch_comp/', views.GetLogosView.as_view()),
]