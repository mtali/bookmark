from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ImageCreateForm

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
