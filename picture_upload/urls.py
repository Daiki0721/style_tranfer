from django.urls import path
from . import views

app_name = 'picture_upload'
urlpatterns = [
    path('', views.UploadImageCreateView.as_view(), name='index'),
    path('result', views.UploadImageListView.as_view(), name='result')
]
