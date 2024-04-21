from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    # REST framework
    path("api/", include("curium_api.user.urls")),
    path("api/org", include("curium_api.organization.urls")),
    path("api/membership", include("curium_api.membership.urls")),
    path("api/volume", include("curium_api.volume.urls")),
]
