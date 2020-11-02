from django.shortcuts import render
from django.views.generic import View
from .forms import UploadImageForm

# Create your views here.
class IndexView(View):
	def get(self, request):
		"""
		view index page
		"""
		form = UploadImageForm()
		context = {
			'form': form
		}
		return render(request, 'base.html', context)
