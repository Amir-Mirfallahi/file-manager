from rest_framework.serializers import ModelSerializer
from .models import File


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': False, 'read_only': True}
        }
