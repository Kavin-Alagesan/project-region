from django.shortcuts import render,redirect
import requests
from django.contrib import messages
from django.http import HttpResponse
import json
from django.conf import settings


url=settings.URL
# Create your views here.

def create(request):
    if request.method=='POST':
        region_code=request.POST['txtRegionCode']
        region_name=request.POST['txtRegionName']
        country=request.POST['ddlCountry']
        image=request.FILES.get('fileImage')
        data={
            'code':region_code,
            'name':region_name,
            'country':country,
            }
        file={
            'image':image
        }
        response=requests.post('{url}'.format(url=url), data=data,files=file)
        print(data)
        print(file)
        print(response.text)
        get_response = response.json()
        if response.status_code > 300:
            print(response)
            print(data)
            print(file)
            messages.error(request,'Fill according to instructions')
            response_data=requests.get('{url}show_api_region/'.format(url=url)).json()
            return render(request,'region/create.html',{'data_list':response_data,'response':get_response,'return_data':data,'return_img':file})
        else:
            messages.success(request,("Region data entered successfully"))
            return redirect('create')
    else:
        response=requests.get('{url}show_api_region/'.format(url=url)).json()
        data = response
        return render(request,'region/create.html',{'data_list':data})

def update(request,id):
    if request.method=='POST':
        region_code=request.POST['txtRegionCode']
        region_name=request.POST['txtRegionName']
        country=request.POST['ddlCountry']
        image=request.FILES.get('fileImage')
        data={
            'code':region_code,
            'name':region_name,
            'country':country,
            }
        file={
            'image':image
        }
        print('UPLOAD IMAGE::::', image)
        response=requests.put('{url}show_api_region/{pk}/'.format(url=url, pk=id), data=data,files=file)
        print('-------update-------')
        print(response)
        print(data)
        get_response = response.json()
        if response.status_code > 300:
            print(response)
            messages.error(request,'Fill according to instructions')
            response_data=requests.get('{url}show_api_region/'.format(url=url)).json()
            return render(request,'region/create.html',{'data_list':response_data,'response':get_response,'return_data':data})
        else:
            messages.success(request,("Data updated successfully"))
            return redirect('create')
    else:
        response=requests.get('{url}show_api_region/'.format(url=url)).json()
        data = response
        return render(request,'region/create.html',{'data':data})

def delete(request,id):
    response=requests.delete("{url}{pk}".format(url=url, pk=id))
    messages.success(request,("Region details deleted successfully"))
    return redirect('create')

