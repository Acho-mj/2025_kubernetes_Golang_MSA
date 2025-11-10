from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    """
    Category 데이터 직렬화/역직렬화 Serializer.
    """

    id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField(allow_null=True, required=False)


