from rest_framework import serializers
from.models import *

class turistserializer(serializers.ModelSerializer):
    class Meta:
        model = turiste
        fields = "__all__"

class visitorserializer(serializers.ModelSerializer):
    class Meta:
        model = visitor
        fields = "__all__"