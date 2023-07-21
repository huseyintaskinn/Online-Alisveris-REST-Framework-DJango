from rest_framework import serializers
from Kiyafetler.models import Kiyafet, Puan

class PuanSerializer(serializers.ModelSerializer):
    Puan_sahibi = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Puan
        # fields = '__all__'
        exclude = ['Kiyafet']

class KiyafetSerializer(serializers.ModelSerializer):
    Puanlar = PuanSerializer(many=True, read_only=True)
    class Meta:
        model = Kiyafet
        fields = '__all__'


