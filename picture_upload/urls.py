from django.urls import path
from . import views

app_name = 'picture_upload'
urlpatterns = [
    path('', views.UploadImageCreateView.as_view(), name='index'),
    path('result/<int:pk>/', views.UploadImageDetailView.as_view(), name='result'),
]
