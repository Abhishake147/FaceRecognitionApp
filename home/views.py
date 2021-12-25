from django.shortcuts import render, redirect
from .form import ImageForm
from .models import Image

from subprocess import run, PIPE
import sys

import cv2

# Create your views here.

def homePage(request):
    return render(request, 'homePage.html')

def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "index.html", {"obj": obj})
    else:
        form = ImageForm()
    img = Image.objects.all()
    return render(request, "index.html", {"img": img, "form": form})


def screenshots(request):
    output = run([sys.executable, 'C://Users//crazy//PycharmProjects//ImageformProject//webcam_screenshots.py'], shell=False, stdout=PIPE)
    return render(request, 'index.html', {'data1':output.stdout})



def authentication(request):
    output = run([sys.executable, 'C://Users//crazy//PycharmProjects//ImageformProject//Face_Recognition.py'], shell=False, stdout=PIPE)
    return render(request, 'Authentication.html', {'data1': output.stdout})





