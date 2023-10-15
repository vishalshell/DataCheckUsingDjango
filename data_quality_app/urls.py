from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('download_failed_rows/', views.download_failed_rows, name='download_failed_rows'),
]
