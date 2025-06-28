from PIL import Image, UnidentifiedImageError
from django.core.files.base import ContentFile
from io import BytesIO
import os

class ImageProcessingService:
    @staticmethod
    def process_image(form, img_file):
        try:
            upload_img = form.save(commit=False)

            # Verify and reopen image
            img = Image.open(img_file)
            img.verify()

            img_file.seek(0)
            img = Image.open(img_file).convert('RGBA')

            # Generate thumbnail
            thumb = img.copy()
            thumb.thumbnail((100, 100))
            thumb_io = BytesIO()
            thumb.save(thumb_io, format='PNG')

            upload_img.save()

            original_name = os.path.basename(upload_img.image.name)
            thumb_name = f"thumb_{original_name}"
            upload_img.thumbnail.save(thumb_name, ContentFile(thumb_io.getvalue()), save=False)

            # Crop img & extract color
            img_crop = ImageProcessingService._crop_image(img)
            img.close()

            if img_crop is None:
                raise ValueError('Image cropping failed.')

            pxl_color = ImageProcessingService._extract_color(img_crop)
            if not pxl_color:
                raise ValueError('Pixel color extraction failed.')

            upload_img.hex_color = pxl_color
            upload_img.save()

            return {'upload_img': upload_img, 'hex_color': pxl_color}

        except UnidentifiedImageError:
            print('Invalid File Type. Please upload a valid image (e.g., jpeg, png, etc.)')
        except Exception as e:
            print(f'Unexpected Error: {e}')
        return {}

    # Func to crop image while maintaining exact centre pos for memory efficiency -> gets 1x1 or 2x2 img
    @staticmethod
    def _crop_image(img: Image.Image) -> Image.Image | None:
        try:
            width, height = img.size
            centre_x, centre_y = width // 2, height // 2 # Calc coordinates for centre pxl

            # For img with even dimensions:
            if width % 2 == 0 and height % 2 == 0:
                left = max(centre_x - 1, 0)
                upper = max(centre_y - 1, 0)
                right = min(centre_x + 1, width)
                lower = min(centre_y + 1, height)
                img_crop = (left, upper, right, lower)
            else:
                img_crop = (centre_x, centre_y, centre_x + 1, centre_y + 1)

            cropped_img = img.crop(img_crop)
            
            return cropped_img
        except Exception as e:
            print(f'Image cropping failed {e}')
            return None
        

    # Func to extract centre most or avg of 4 centre most pixels in hex format
    @staticmethod
    def _extract_color(img_crop: Image.Image) -> str | None:
        try:
            pxls = list(img_crop.getdata())
            total_pxls = len(pxls)

            # Will get centre pxl for both 1x1 and 2x2 crop
            sum_r = sum_g = sum_b = 0
            for pxl in pxls:
                r, g, b = pxl[:3]
                sum_r += r
                sum_g += g
                sum_b += b

            avg_r = sum_r // total_pxls
            avg_g = sum_g // total_pxls
            avg_b = sum_b // total_pxls

            # Covnert RGB to Hex:
            hex_color = f'#{avg_r:02x}{avg_g:02x}{avg_b:02x}'
            return hex_color
        
        except Exception as e:
            print(f'Image color extraction failed {e}')
            return None