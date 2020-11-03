from django import forms
from django.core.validators import FileExtensionValidator


class UploadImageForm(forms.Form):
	"""
	form to multiple image upload
	"""
	image = forms.ImageField(
			widget=forms.FileInput(attrs={'multiple': True}),
			required=True,
			validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])]
	)
