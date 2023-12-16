from django.shortcuts import render
from django.urls import reverse_lazy
from .models import UploadImage, Styles
from django.views import generic
from .forms import UploadImageForm


class UploadImageCreateView(generic.CreateView):
    model = UploadImage
    template_name = 'index.html'
    form_class = UploadImageForm
    success_url = reverse_lazy('picture_upload:result')
    extra_context = {
        "list": Styles.objects.all(),
    }
    
class UploadImageListView(generic.ListView):
    model = UploadImage
    template_name = 'result.html'
    paginate_by = 10
    extra_context = {
        "list": Styles.objects.all(),
    }