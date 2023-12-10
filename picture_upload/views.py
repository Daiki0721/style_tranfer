from django.shortcuts import render
from django.urls import reverse_lazy
from .models import PictureUpload
from django.views import generic
from .forms import PictureUploadForm


class PictureUploadCreateView(generic.CreateView):
    model = PictureUpload
    template_name = 'index.html'
    form_class = PictureUploadForm
    success_url = reverse_lazy('picture_upload:result')

class PictureUploadListView(generic.ListView):
    model = PictureUpload
    template_name = 'result.html'
