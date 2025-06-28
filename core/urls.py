from django.urls import path
from .views import home, upload_image_api, list_images, image_detail

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_image_api, name='upload'),
    path('images/', list_images, name='list_images'),
    path('images/<int:image_id>/', image_detail, name='image_detail'),
]