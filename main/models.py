from django.db import models

# Create your models here.
class Picture(models.Model):
	img = models.ImageField(upload_to='images', verbose_name='Файл изображения')

	def __str__(self):
		return self.img.url
	
	class Meta:
		verbose_name = 'Изображение'
		verbose_name_plural = 'Изображения'
