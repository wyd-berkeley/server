from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'first_name', 'last_name')
		lookup_field = ('username',)
		read_only_fields = ('username',)
		write_only_fields = ('password',)

	def create(self, validated_data):
		return User.objects.create(**validated_data)

	def retrieve(self, validated_data):
		return self.get_object()
