from django.db import models
import os
from django.core.exceptions import ValidationError


def validate_is_picture(value):
    ext = os.path.splitext(value.name)[1]

    if not ext.lower() in ['.jpg', '.png', '.jpeg']:
        raise ValidationError('Only picure files are availables.')

MAX_SIZE    = 1 * 1000 * 1000

def validate_max_size(value):
    if value.size > MAX_SIZE:
        print('ファイルサイズが上限' + str(MAX_SIZE/1000000) + 'MBを超えています。送信されたファイルサイズ: ' + str(value.size/1000000) + "MB")
        raise ValidationError( "ファイルサイズが上限(" + str(MAX_SIZE/1000000) + "MB)を超えています。送信されたファイルサイズ: " + str(value.size/1000000) + "MB")

    else:
        print("問題なし")


class Styles(models.Model):
    style_image = models.ImageField(verbose_name='style_image',upload_to='styles_img/',)
    style_num = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Styles'


class UploadImage(models.Model):
    contents_image = models.ImageField(verbose_name='contents_image', upload_to='img/', validators=[validate_is_picture, validate_max_size],)
    style_num = models.ForeignKey(Styles, on_delete=models.CASCADE)
    created_image = models.ImageField(verbose_name='created_image',upload_to='created_img/',)

    class Meta:
        verbose_name_plural = 'UploadImage'
