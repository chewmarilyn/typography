from django.http.response import JsonResponse
from django.shortcuts import render

from type.models import TypeImage, UserImage


def home(request):
    all_type_image = TypeImage.objects.order_by('-priority')
    info = [{
        'name': image.name,
        'description': image.description,
        'url': image.image.url
    }
        for image in all_type_image
    ]
    return render(request, 'type/index.html', {'images': info})


def upload(request):
    uploaded_file = request.FILES.get('image')
    if uploaded_file:
        image_meta = UserImage.store_image(uploaded_file)
        return JsonResponse(image_meta)
    return JsonResponse({})
