# Generated by Django 4.2.7 on 2023-12-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture_upload', '0006_alter_styles_style_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='styles',
            name='style_image',
            field=models.ImageField(upload_to='', verbose_name='style_image'),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='contents_image',
            field=models.ImageField(upload_to='img/', verbose_name='contents_image'),
        ),
    ]