from .serializers import FileSerializer
from .models import File
from rest_framework.generics import *


class FileListCreateApiView(ListCreateAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def get_queryset(self):
        print(self.request.user)
        return File.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user when creating a new file
        serializer.save(user=self.request.user)


class FileRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
