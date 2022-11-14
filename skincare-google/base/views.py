import base64
from django.conf import settings
from .forms import ImageUploadForm
from django.shortcuts import render
from .models import *
from django.http.response import StreamingHttpResponse
import time
# Create your views here.


def home(request):
    context = {}
    return render(request, 'base/home.html', context)


def use(request):
    context = {}
    return render(request, 'base/use.html', context)


def about(request):
    context = {}
    return render(request, 'base/about.html', context)


def skintype(request):
    image_uri = None
    predicted_label = None
    imd = None
    # start = time.time()
    if request.method == 'POST':
        # in case of POST: get the uploaded image from the form and process it
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # retrieve the uploaded image and convert it to bytes (for PyTorch)
            image = form.cleaned_data['image']
            image_bytes = image.file.read()
            encoded_img = base64.b64encode(image_bytes)
            decoded_img = encoded_img.decode("ascii")
            image_uri = 'data:%s;base64,%s' % ('image/jpeg', decoded_img)
            # image_link = base2picture(image_uri)
            try:
                predicted_label, ans = skin(decoded_img, 'django')
                # predicted_label, ans = skin(image_link, 'url')
                # end = time.time()
                # print(format(end-start))
            except RuntimeError as re:
                print(re)
            print(predicted_label)
            imd = plot_pie(predicted_label)
    else:
        # in case of GET: simply show the empty form for uploading images
        form = ImageUploadForm()

    # pass the form, image URI, and predicted label to the template to be rendered
    context = {
        'form': form,
        'image_uri': image_uri,
        'predicted_label': predicted_label,
        'img': imd,
    }
    return render(request, 'base/skin-type.html', context)


def nailtest(request):
    image_uri = None
    predicted_label = None
    imd = None
    if request.method == 'POST':
        # in case of POST: get the uploaded image from the form and process it
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # retrieve the uploaded image and convert it to bytes (for PyTorch)
            image = form.cleaned_data['image']
            image_bytes = image.file.read()

            encoded_img = base64.b64encode(image_bytes)
            decoded_img = encoded_img.decode()
            image_uri = 'data:%s;base64,%s' % ('image/jpeg', decoded_img)
            # image_link = base2picture(image_uri)
            try:
                predicted_label, ans = nail(decoded_img, 'django')
                # predicted_label, ans = nail(image_link, 'url')
            except RuntimeError as re:
                print(re)
            # print(predicted_label)
            if list(ans.keys())[0] == 'normalnail':
                imd = 'low'
            else:
                imd = 'high'
    else:
        # in case of GET: simply show the empty form for uploading images
        form = ImageUploadForm()

    # pass the form, image URI, and predicted label to the template to be rendered
    context = {
        'form': form,
        'image_uri': image_uri,
        'predicted_label': predicted_label,
        'img': imd,
    }
    return render(request, 'base/nail-test.html', context)
# Create your views here.


def acnetest(request):
    image_uri = None
    ans = None
    imd = None
    if request.method == 'POST':
        # in case of POST: get the uploaded image from the form and process it
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # retrieve the uploaded image and convert it to bytes (for PyTorch)
            image = form.cleaned_data['image']
            image_bytes = image.file.read()

            encoded_img = base64.b64encode(image_bytes)
            decoded_img = encoded_img.decode()
            image_uri = 'data:%s;base64,%s' % ('image/jpeg', decoded_img)
            # image_link = base2picture(image_uri)
            try:
                predicted_label, ans = acne(decoded_img, 'django')
                # predicted_label, ans = nail(image_link, 'url')
            except RuntimeError as re:
                print(re)
            # print(predicted_label)
            if ans == 'Mild':
                imd = 'mild'
            elif ans == 'Moderate':
                imd = 'moderate'
            elif ans == 'Severe':
                imd = 'severe'
            else:
                imd = 'Very-Severe'
    else:
        # in case of GET: simply show the empty form for uploading images
        form = ImageUploadForm()

    # pass the form, image URI, and predicted label to the template to be rendered
    context = {
        'form': form,
        'image_uri': image_uri,
        'predicted_label': ans,
        'img': imd,
    }
    return render(request, 'base/acne-test.html', context)


# Create your views here.


# def index(request):
#     return render(request, 'base/camera.html')


# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# def camera_feed(request):
#     return StreamingHttpResponse(gen(ImageDetect()),
#                                  content_type='multipart/x-mixed-replace; boundary=frame')
