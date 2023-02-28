from django.urls import path
from . import views


app_name = "leitner"

urlpatterns = [path("", views.LeitnerBoxList.as_view(), name="leitner")]
