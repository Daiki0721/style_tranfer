import tensorflow as tf

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .models import UploadImage, Styles
from django.views import generic
from .forms import UploadImageForm
from model import generate_images

class UploadImageCreateView(generic.CreateView):
    model = UploadImage
    template_name = 'index.html'
    form_class = UploadImageForm
    extra_context = {
        "list": Styles.objects.all(),
    }

    def get_success_url(self):
        return reverse('picture_upload:result', kwargs={'pk':self.object.pk})

class UploadImageDetailView(generic.DetailView):
    model = UploadImage
    template_name = 'result.html'

class UploadImageListView(generic.ListView):
    model = UploadImage
    template_name = 'list_result.html'
    paginate_by = 10
