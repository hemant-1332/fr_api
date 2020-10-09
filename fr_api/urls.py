from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns =[
    path(r'^face_detection/detect/$', 'face_detector.views.detect'),
    path(r'^admin/', include(admin.site.urls))
]

