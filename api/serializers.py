from rest_framework import serializers
from api.models import Keyword, KeywordTag


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['keyword_tag'] = f"{instance.keyword_tag.name}"
        return response


class KeywordTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordTag
        fields = "__all__"


class ParserSerializer(serializers.Serializer):
    summary = serializers.CharField(required=True)
    experiences = serializers.ListField(required=True)
    educations = serializers.ListField(required=True)
    certifications = serializers.ListField(required=True)
    requests = serializers.ListField(required=True)
