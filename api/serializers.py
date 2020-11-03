from rest_framework import serializers
from main.models import Picture


class PictureSerializer(serializers.ModelSerializer):
	"""
	serializer for Picture model
	"""
	class Meta:
		model = Picture
		fields = ['id', 'img', 'width', 'height', 'extension', 'thumbnail', 'uploaded_at']
