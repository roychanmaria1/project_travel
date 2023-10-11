from django.contrib import admin
from django.urls import path
from .import views

from  travel_project import settings
from  django.conf.urls.static import static

urlpatterns = [
    path('',views.demo,name='demo'),
    path('',views.sample,name='sample'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
