#import tensorflow as tf

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .models import UploadImage, Styles
from django.views import generic
from .forms import UploadImageForm
import cv2
from config import settings_dev

import os

#ai_model = tf.keras.models.load_model('../my_model.h5')

def gray(input_url,output_url):
    img = cv2.imread(input_url)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_url, img_gray)

class UploadImageCreateView(generic.CreateView):
    model = UploadImage
    template_name = 'index.html'
    form_class = UploadImageForm
    extra_context = {
        "list": Styles.objects.all(),
    }

    def form_valid(self, form):
        #アップされたインスタンスを持ってくる
        data = form.cleaned_data
        print(dir(data))
        print(data)
        obj = self.model(**data)
        obj.save()
        print(obj.contents_image.name)
        print(obj.id)
        #白黒変換
        input_url = str(settings_dev.BASE_DIR) + obj.contents_image.url
        output_url = str(settings_dev.BASE_DIR) + "/media/created_img/" + str(obj.id) + ".jpg"
        print(input_url)
        print(output_url)
        gray(input_url, output_url)
        #データベースに加工した画像を登録
        obj.created_image = "/created_img/" + str(obj.id) + ".jpg"
        #ここで最初の保存
        obj.save()
        print(obj.created_image.url)
       
        return super().form_valid(form) 
    

    def get_success_url(self):
        print(self.object)
        return reverse('picture_upload:result', kwargs={'pk':self.object.pk})
        #ここで二個目のデータベースへの保存(createviewのPOSTの効果)


class UploadImageDetailView(generic.DetailView):
    model = UploadImage
    template_name = 'result.html'

       
            

class UploadImageListView(generic.ListView):
    model = UploadImage
    template_name = 'list_result.html'
    paginate_by = 10
