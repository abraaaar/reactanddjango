from django.urls import path
from .views import volume_view, volume_record_view

urlpatterns = [
    path("", volume_view, name="volume"),
    path("<uuid:pk>", volume_record_view, name="volume_record"),
]
