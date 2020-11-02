from django import forms


class UploadImageForm(forms.Form):
	"""
	form to multiple image upload
	"""
	image = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}), required=True)
