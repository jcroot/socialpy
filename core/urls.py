from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('request', views.post_request, name="post_request"),
]
