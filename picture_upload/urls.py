from django.urls import path
from . import views

app_name = 'picture_upload'
urlpatterns = [
    path('', views.PictureUploadCreateView.as_view(), name='index'),
    path('result', views.PictureUploadListView.as_view(), name='result')
]
