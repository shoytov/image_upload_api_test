from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from api.services.upload_files import UploadFiles
from api.services.get_all_images import GetAllImages
from api.services.get_image_by_id import GetImageById
from api.services.delete_picture import DeletePicture
from main.forms import UploadImageForm


# Create your views here.
class Image(APIView):
	def get(self, request):
		"""
		endpoint to get all images data
		"""
		return Response(GetAllImages.get(), HTTP_200_OK)
	
	def post(self, request):
		"""
		endpoint to upload files
		"""
		form = UploadImageForm(request.POST, request.FILES)
		if form.is_valid():
			UploadFiles.upload(request.FILES)
			return Response(HTTP_201_CREATED)
		
		return Response({'data': 'Not allowed extension'}, HTTP_400_BAD_REQUEST)
	
	
class CurrentImage(APIView):
	def get(self, request, picture_id: int):
		"""
		get data for one picture
		"""
		res = GetImageById.get(picture_id)
		if len(res) > 0:
			return Response(res, HTTP_200_OK)
		else:
			return Response(status=HTTP_404_NOT_FOUND)
		
	def delete(self, request, picture_id: int):
		"""
		delete picture
		"""
		DeletePicture.delete(picture_id)
		return Response(status=HTTP_204_NO_CONTENT)
