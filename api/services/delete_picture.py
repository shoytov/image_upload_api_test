from django.core.exceptions import ObjectDoesNotExist
from main.models import Picture


class DeletePicture(object):
	@staticmethod
	def delete(picture_id: int) -> None:
		"""
		delete picture by id
		"""
		try:
			picture = Picture.objects.get(pk=int(picture_id))
			picture.delete()
		except ObjectDoesNotExist:
			pass
