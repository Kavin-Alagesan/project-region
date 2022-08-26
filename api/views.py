from rest_framework import generics
from api.models import Regionmodel
from api.serializers import RegionSerializer,ShowRegionSerializer

class RegionListCreateAPI(generics.ListCreateAPIView):
    queryset=Regionmodel.objects.all()
    serializer_class=RegionSerializer

class RegionUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Regionmodel.objects.all()
    serializer_class=RegionSerializer

class ShowRegion(generics.ListAPIView):
    queryset=Regionmodel.objects.all()
    serializer_class=ShowRegionSerializer

class UpdateRegion(generics.RetrieveUpdateAPIView):
    queryset=Regionmodel.objects.all()
    serializer_class=ShowRegionSerializer

