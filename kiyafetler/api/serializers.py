from rest_framework import serializers
from kiyafetler.models import Kiyafet, Puan
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email')
        extra_kwargs = {
            'password': {'write_only': True}, 
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user

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



