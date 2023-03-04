from rest_framework import  mixins, generics

from .serializers import PDF2DOCXSerializer
from .models import FileUpload


class PDF2DOCXView( mixins.ListModelMixin ,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = PDF2DOCXSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

     