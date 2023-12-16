from django.db import models


class Styles(models.Model):
    style_image = models.ImageField(verbose_name='style_image',upload_to='styles_img/',)
    style_num = models.IntegerField()


class UploadImage(models.Model):
    contents_image = models.ImageField(verbose_name='contents_image', upload_to='img/',)
    style_num = models.ForeignKey(Styles, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'UploadImage'

