from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("configure", views.configure, name="configure"),
    path("saveConfiguration", views.saveConfiguration, name="saveConfiguration")
]