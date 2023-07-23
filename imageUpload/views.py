# views.py
from django.shortcuts import render, redirect

from .forms import UploadImageForm
from .models import UploadedImage


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect('uploaded_image',
                            pk=instance.pk)  # Redirect to the uploaded_image view with the uploaded image's primary key (pk)
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form})


def uploaded_image(request, pk):
    instance = UploadedImage.objects.get(pk=pk)
    return render(request, 'uploaded_image.html', {'instance': instance})
