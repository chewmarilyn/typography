from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import redirect, render

from chewmarilyn.models import TypeImage, UserImage


def favicon(request):
    return redirect(settings.STATIC_URL + 'favicon.ico')


def home(request):
    all_type_image = TypeImage.objects.order_by('-priority')
    info = [{
        'name': image.name,
        'description': image.description,
        'url': image.image.url
    }
        for image in all_type_image
    ]
    return render(request, 'chewmarilyn/index.html', {'images': info})


def upload(request):
    uploaded_file = request.FILES.get('image')
    if uploaded_file:
        image_meta = UserImage.store_image(uploaded_file)
        return JsonResponse(image_meta)
    return JsonResponse({})
