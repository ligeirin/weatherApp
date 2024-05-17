from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("configure", views.configure, name="configure"),
    path("saveConfiguration", views.saveConfiguration, name="saveConfiguration")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)