import os

from django.views import generic
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

from .models import DataInfo
from .forms import DataInfoForm

class DataListView(generic.ListView):
    model = DataInfo

class UploadView(generic.CreateView):
    model = DataInfo
    success_url = reverse_lazy('datainfo_list')
    form_class = DataInfoForm
    template_name = 'managedata/upload.html'
    


class DownloadView(generic.View):
    # Here set the name of the file with extension
    file_name = ''
    # Set the content type value
    content_type_value = 'image/jpeg'

    def get(self, request, file_name):
        print(file_name)
        self.file_name = file_name
        file_path = os.path.join('data', self.file_name)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(
                    fh.read(),
                    content_type=self.content_type_value
                )
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
        else:
            raise Http404