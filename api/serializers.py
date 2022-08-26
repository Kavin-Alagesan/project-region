from rest_framework import serializers
from .models import Regionmodel
from django.core.exceptions import ValidationError

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Regionmodel
        fields=['id','code','name','country','image']

    def validate(self,data):
        if data.get('name'):
            for data_name in data.get('name'):
                if data_name.isdigit():
                    raise serializers.ValidationError({'name':'Region name must not be numeric'})
        if data.get('code'):
            code2=data.get('code')
            user_qs=Regionmodel.objects.filter(code=code2)
            if user_qs.exists():
                raise ValidationError({'code':'Region code already exists'})
        if data.get('name'):
            name_qs=Regionmodel.objects.filter(name=data.get('name'))
            if name_qs.exists():
                raise serializers.ValidationError({'name':'Region name already exists'})
        if data.get('country'):
            country_qs=data.get('country')
            if (country_qs == "0"):
                raise serializers.ValidationError({'country':'Country should select'})
        return data
        
class ShowRegionSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='get_country_display')
    class Meta:
        model=Regionmodel
        fields=['id','code','name','country','image']

    def validate(self,data):
        if data.get('name'):
            for n in data.get('name'):
                if n.isdigit():
                    raise serializers.ValidationError({'name':'Region name must not be numeric'})
        if data.get('country'):
            country_qs=data.get('country')
            if (country_qs == "0"):
                raise serializers.ValidationError({'country':'Country should select'})
        return data
        