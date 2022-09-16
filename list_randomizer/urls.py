from django.urls import re_path
from django.contrib import admin
from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.button),
    re_path(r'^output', views.output, name="script"),
]
