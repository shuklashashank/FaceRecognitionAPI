
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib import admin
from face_detector import views

urlpatterns = [
    # Examples:

    url(r'^face_detection/recognize/$', views.recognize),
    url(r'^face_detection/train/$', views.train),
    url(r'^face_detection/new/$', views.new),
    url(r'^face_detection/users/$', views.users),
    url(r'^admin/', admin.site.urls),
]
