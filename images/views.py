from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .forms import ImageCreateForm
from .models import Image

@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            instance = form.save(commit=False)

            # assigning user
            instance.user = request.user
            instance.save()
            messages.success(request, 'Image added successfully')

            # redirecting to new created image detail view
            return redirect(instance.get_absolute_url())
    else:
        form = ImageCreateForm(request.GET)

    return render(request, 'images/image/create.html',
                        {'section': 'images','form': form})

def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html',
            {'section': 'images', 'image': image})
