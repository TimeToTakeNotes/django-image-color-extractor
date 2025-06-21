from django.urls import path
from .views import home, upload_image, list_images, image_detail

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_image, name='upload'),
    path('images/', list_images, name='list_images'),
    path('images/<int:image_id>/', image_detail, name='image_detail'),
]