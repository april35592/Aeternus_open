from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password, check_password
from .models import Image, Reply
from .forms import ImageForm, ReplyForm
import hashlib

def diary(request):
    page = request.GET.get('page', '1')
    image_list = Image.objects.order_by('-id')
    paginator = Paginator(image_list, 5)
    page_obj = paginator.get_page(page)
    image_form = ImageForm
    return render(
        request,
        'diary/diary_list.html',
        {
            'image_list' : page_obj,
            'reply_set' : Reply,
            'image_form' : image_form,
        })


def uploadImage(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.password = make_password(image.password)
            image.save()
    return redirect('diary:main')


def deleteImage(request, image_id):
    if request.method == 'POST':
        image = get_object_or_404(Image, pk=image_id)
        if request.POST['password'] != '':
            if check_password(request.POST['password'], image.password):
                image.delete()
    return redirect('diary:main')


def createReply(request, image_id):
    if request.method == 'POST':
        image = get_object_or_404(Image, pk=image_id)
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.imageid = image
            reply.password = make_password(reply.password)
            reply.save()
    return redirect('diary:main')


def deleteReply(request, reply_id):
    if request.method == 'POST':
        reply = get_object_or_404(Reply, pk=reply_id)
        if request.POST['password'] != '':
            if check_password(request.POST['password'], reply.password):
                reply.delete()
    return redirect('diary:main')