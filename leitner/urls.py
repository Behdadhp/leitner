from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("leitner/", include("box.urls", namespace="leitner")),
]
