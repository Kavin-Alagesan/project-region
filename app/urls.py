from django.urls import path
from app import views

urlpatterns = [
    path('',views.create,name="create"),
    path('update/<id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),
]
