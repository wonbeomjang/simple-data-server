from django.urls import path
from django.conf.urls import url
from django.core.files.storage import FileSystemStorage
from django_downloadview import StorageDownloadView, ObjectDownloadView

from . import views
from .models import DataInfo# A model with a FileField

urlpatterns = [
    path('', views.DataListView.as_view(), name='datainfo_list'),
    path('upload/', views.UploadView.as_view(), name='data_upload'),
    path('download/<int:pk>', ObjectDownloadView.as_view(model=DataInfo, file_field='data_file'), name='download'),
]