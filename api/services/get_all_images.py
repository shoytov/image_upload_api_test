from collections import OrderedDict
from main.models import Picture
from api.serializers import PictureSerializer


class GetAllImages(object):
	@staticmethod
	def get() -> OrderedDict:
		"""
		get all images in db and make serialized data to response
		"""
		images = Picture.objects.all()
		serializer = PictureSerializer(images, many=True)
		print(serializer.data)
		return serializer.data
