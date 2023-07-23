# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_uploaded_images, name='view_uploaded_images'),
    path('upload/', views.upload_image, name='upload_image'),
    path('uploaded_image/<int:pk>/', views.uploaded_image, name='uploaded_image'),
]
