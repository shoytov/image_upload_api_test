from django.shortcuts import render
from django.views.generic import View
from .forms import UploadImageForm
from .models import Picture


# Create your views here.
class IndexView(View):
	def get(self, request):
		"""
		view index page
		"""
		form = UploadImageForm()
		images = Picture.objects.all()
		
		context = {
			'form': form,
			'images': images
		}
		return render(request, 'base.html', context)
