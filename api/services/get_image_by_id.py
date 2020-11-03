from django.core.exceptions import ObjectDoesNotExist
from main.models import Picture
from api.serializers import PictureSerializer


class GetImageById(object):
	@staticmethod
	def get(picture_id: int) -> dict:
		"""
		make data for one picture
		"""
		try:
			image = Picture.objects.get(pk=int(picture_id))
			serializer = PictureSerializer(image)
			result = serializer.data
		except ObjectDoesNotExist:
			result = {}
			
		return result
