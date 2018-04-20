from rest_framework import serializers
from api.models import BlogApi

class BlogSerializer(serializers.ModelSerializer):

	class Meta:
		model = BlogApi
		fields = '__all__'