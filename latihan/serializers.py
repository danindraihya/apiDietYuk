from rest_framework import serializers
from .models import Latihan, Olahraga

class OlahragaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Olahraga
        fields = ['id', 'jenis', 'waktu']
        extra_kwargs = {'books' : {'required' : False}}


class LatihanSerializer(serializers.ModelSerializer):
    olahraga = OlahragaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Latihan
        fields = ['id', 'hari', 'total_waktu', 'olahraga']
        # extra_kwargs = {'olahraga' : {'required' : False}}