from rest_framework.serializers import ModelSerializer

from .models import Query
from .services import server


class QuerySerializer(ModelSerializer):
    def create(self, validated_data):
        result = server()
        validated_data['result'] = result
        return super().create(validated_data)

    class Meta:
        model = Query
        fields = '__all__'