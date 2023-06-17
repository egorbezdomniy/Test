from rest_framework import serializers
from . import models

class LiquidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['name', 'amount', 'brand', 'price', 'margin', 'description']
        model = models.Liquid


class SingleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['name', 'amount', 'brand', 'price', 'margin', 'description']
        model = models.Single


class PodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['name', 'amount', 'brand', 'price', 'margin', 'description', 'battery']
        model = models.Pod


class EvaporatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['name', 'amount', 'brand', 'price', 'margin', 'description']
        model = models.Evaporator


class LiquidBrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['name', 'description']
        model = models.LiquidBrand


class SingleBrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['name', 'description']
        model = models.SingleBrand


class PodBrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['name', 'description']
        model = models.PodBrand


class EvaporatorBrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['name', 'description']
        model = models.EvaporatorBrand


