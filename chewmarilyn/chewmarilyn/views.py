import base64

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def download(request):
    image_data = request.POST.get('data')
    base64_data = image_data.split(',')[-1]
    data = base64.b64decode(base64_data)
    suf = SimpleUploadedFile('temp.png', data)
    image_meta = UserImage.store_image(suf)
    return JsonResponse(image_meta)
