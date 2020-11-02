from django.urls import path
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from .views import ImageUpload


schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
	path('schema/', get_schema_view(
			title="Image Upload service",
			description="API for all things",
	), name='openapi-schema'),
	path('test', ImageUpload.as_view()),
	path('swagger/', schema_view)
]
