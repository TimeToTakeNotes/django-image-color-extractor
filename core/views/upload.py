from django.shortcuts import render
from core.forms import ImageUploadForm
from core.services import ImageProcessingService
            
# Main func for uploading and showing img
def upload_image_api(request):
    # Vars. defined before POST to prevent error:
    upload_img = None
    pxl_color = None

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            img_file = request.FILES['image']
            result = ImageProcessingService.process_image(form, img_file) # All image processing from service

            upload_img = result.get('upload_img')
            pxl_color = result.get('hex_color')
    else:
        form = ImageUploadForm()

    return render(request, 'upload_form.html', {
        'form': form,
        'uploaded_image': upload_img,
        'hex_color': pxl_color
    })