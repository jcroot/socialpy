from django.urls import include, path
from rest_framework import routers
from core import api as core_api

PREFIX = "api/v1"

router = routers.DefaultRouter()
router.register(r'users', core_api.UserViewSet)
router.register(r'groups', core_api.GroupViewSet)
router.register(r'check', core_api.PostRequestViewSet)
router.register(r'review', core_api.NangarekoViewSet)

urlpatterns = [
    path(f"{PREFIX}/", include(router.urls)),
]
