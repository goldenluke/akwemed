from django.urls import path
from .views import consult

urlpatterns = [
    path("consult/", consult)
]
