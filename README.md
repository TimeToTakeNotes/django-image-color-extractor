# Django Image Color Extractor

This Django application allows users to upload images and automatically extracts the color at the center (or average of the center 4 pixels) of each uploaded image. The extracted hex color and the image are stored using a simple model and displayed through Django's templating system.

---

## Features

- Upload images through a simple web form.
- Extract centre or average centre 2x2 pixels' hex color.
- Store image and hex color in the Django built-in sqlite database.
- View a list of all uploaded images and their extracted hex colors.
- Click an image to view a detailed page with a color swatch.
- Basic error handling.

---

## Tech Stack

- Python 3.12+
- Django 5.x
- Django Templates for Frontend
- Pillow (Python Imaging Library)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/django-image-color-extractor.git
cd django-image-color-extractor
```
### 2. Create & activate the virtual environment
#### Windows
```bash
python -m venv .env
.env\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv .env
source .env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the development server
```bash
python manage.py runserver
```
Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Testing the Application

1. Navigate to the home page.
2. Click Upload an Image.
3. Choose an image and submit the form.
4. You’ll be redirected to a preview with the uploaded image and the extracted color.
5. Navigate to /images/ to view all uploaded images and colors.
