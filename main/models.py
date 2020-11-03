from django.db import models
from django.utils.timezone import now


# Create your models here.
class Picture(models.Model):
	img = models.ImageField(upload_to='images', verbose_name='Файл изображения')
	width = models.IntegerField(verbose_name='Ширина изображения', db_index=True)
	height = models.IntegerField(verbose_name='Высота изображения', db_index=True)
	extension = models.CharField(max_length=5, verbose_name='Расширение', db_index=True)
	thumbnail = models.ImageField(upload_to='images', verbose_name='Миниатюра изображения')
	uploaded_at = models.DateTimeField(default=now, verbose_name='Дата и время загрузки', db_index=True)

	def __str__(self):
		return self.img.url
	
	class Meta:
		verbose_name = 'Изображение'
		verbose_name_plural = 'Изображения'
		ordering = ['-uploaded_at']
