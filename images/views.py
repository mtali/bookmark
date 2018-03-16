from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import ImageCreateForm
from .models import Image
from bookmarks.common.decorators import ajax_required

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
    users_likes = image.users_likes.all()
    return render(request, 'images/image/detail.html',
            {'section': 'images', 'image': image, 'users_likes': users_likes})
@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_likes.add(request.user)
            else:
                image.users_likes.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'ko'})

@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer extract the first page
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # if request is ajax and page is out of range return empty response
            return HttpResponse('')
        # if page is out of range deliver the last page
        images = paginator.page(paginator.num_pages)

    if request.is_ajax():
        return render(request, 'images/image/list_ajax.html', {'images': images})
    return render(request, 'images/image/list.html', {'images': images})
