from django.shortcuts import render, get_object_or_404
from core.models import ImageColor

# Gets all imgs from db:
def list_images(request):
    images = ImageColor.objects.all()
    return render(request, 'list_images.html', {'images': images})

# Gets single img obj using id to show img details:
def image_detail(request, image_id):
    img = get_object_or_404(ImageColor, id=image_id)
    return render(request, 'image_detail.html', {'image': img})