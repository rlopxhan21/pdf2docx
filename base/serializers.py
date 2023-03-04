from rest_framework import serializers
import datetime


from .models import FileUpload

class PDF2DOCXSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"
