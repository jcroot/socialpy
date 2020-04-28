from django.contrib.auth.models import User, Group
from rest_framework import viewsets, filters, generics
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Post, Nangareko
from core.serializers import PostSerializer, NangarekoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return super(PostSearchFilter, self).get_search_fields(view, request)


class PostRequestViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, PostSearchFilter]
    search_fields = ['=cic']


class NangarekoViewSet(viewsets.ModelViewSet):
    queryset = Nangareko.objects.all()
    serializer_class = NangarekoSerializer
    filter_backends = [DjangoFilterBackend, PostSearchFilter]
    search_fields = ['=cic', '=phone']
