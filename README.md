# Upload Images with Django
This repository contains a Django web application that allows users to upload images and view them. Users can also delete uploaded images if needed. The application uses Django's built-in FileField to handle image uploads and store image metadata in the database.

## Features
- User-friendly interface for uploading images.
- Display list of uploaded images along with their metadata (name, uploaded date, size, and mimetype).
- Ability to view individual uploaded images with detailed information.
- Option to delete uploaded images.
## Installation
To run this Django app locally, follow these steps:

Clone the repository:
```bash

git clone https://github.com/your-username/django-image-uploads.git
cd django-image-uploads
```

Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```

Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```
On macOS and Linux:
```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Apply database migrations:
```bash
python manage.py migrate
```

Run the development server:
```bash
python manage.py runserver
```

Open your web browser and navigate to http://127.0.0.1:8000/. The app should be up and running.
