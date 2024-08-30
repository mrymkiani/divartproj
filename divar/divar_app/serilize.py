from .models import Advertisment
from rest_framework.serializers import ModelSerializer

class AdverSerializer(ModelSerializer):
    class Meta:
        model = Advertisment
        fields = "__all__"
        