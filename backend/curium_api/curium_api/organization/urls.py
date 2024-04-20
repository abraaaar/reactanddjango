from django.urls import path
from .views import organization_view

urlpatterns = [
    path("", organization_view, name="organization")
]
