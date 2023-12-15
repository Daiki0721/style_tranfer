from django.contrib import admin

# Register your models here.
from .models import UploadImage, Styles
# admin.site.register(Document)
admin.site.register(UploadImage)
admin.site.register(Styles)