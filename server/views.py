from django.contrib.auth.models import User
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)
	lookup_field = 'username'
	lookup_value_regex = '[a-zA-Z0-9_@+.-]{1,30}'
