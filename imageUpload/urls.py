# urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('upload/', views.upload_image, name='upload_image'),
    path('uploaded_image/<int:pk>/', views.uploaded_image, name='uploaded_image'),
]