from django.urls import path
from api.views import RegionListCreateAPI,RegionUpdateDelete,ShowRegion,UpdateRegion

urlpatterns = [
    path('api_region/',RegionListCreateAPI.as_view()),
    path('api_region/<int:pk>/',RegionUpdateDelete.as_view()),
    path('api_region/show_api_region/',ShowRegion.as_view()),
    path('api_region/show_api_region/<int:pk>/',UpdateRegion.as_view()),
    ]
