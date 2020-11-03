import os
import shutil
from pathlib import Path
from typing import Iterable
from PIL import Image
from main.models import Picture
from django.conf import settings


class UploadFiles(object):
	@staticmethod
	def upload(files: Iterable) -> None:
		"""
		save uploaded images into db
		"""
		for f in files.getlist('image'):
			path = f.temporary_file_path()
			
			thumbnail_path = '{}'.format(os.path.join(settings.THUMBNAIL_ROOT, Path(path).name))
			os.makedirs(os.path.dirname(settings.THUMBNAIL_ROOT), exist_ok=True)
			shutil.copy2('{}'.format(path), '{}'.format(thumbnail_path))
			
			im = Image.open(thumbnail_path)
			width, height = im.size
			filename, extension = os.path.splitext(thumbnail_path)
			
			ratio = (settings.WIDTH / float(im.size[0]))
			height = int((float(im.size[1]) * float(ratio)))
			image = im.resize((settings.WIDTH, height), Image.ANTIALIAS)
			image.save(thumbnail_path)
			
			picture = Picture()
			picture.img = f
			picture.width = width
			picture.height = height
			picture.extension = extension
			picture.thumbnail = f'{settings.THUMBNAIL_DIR_NAME}/{Path(thumbnail_path).name}'
			picture.save()
