from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MobilSerializer
from .models import Mobil

# Create your views here.
# @api_view(['GET'])
# def apiOverview(request):
#   api_urls = {
#     'List':  '/list-mobil',
#     'Detail view': '/mobil-detail/<int:id>',
#     'Create':  '/mobil-create',
#     'Update':  '/mobil-update/<int:id>',
#     'Delete':  '/mobil-detail/<int:id>',
#   }

#   return Response(api_urls)

@api_view(['GET'])
def showAll(request):
  mobil = Mobil.objects.all()
  serializer = MobilSerializer(mobil, many=True)
  return Response(serializer.data)
  

@api_view(['GET'])
def detailMobil(request, pk):
  mobil = Mobil.objects.get(id=pk)
  serializer = MobilSerializer(mobil, many=False)
  return Response(serializer.data)


@api_view(['POST'])
def createMobil(request):
  serializer = MobilSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@api_view(['POST'])
def updateMobil(request, pk):
  mobil = Mobil.objects.get(id=pk)
  serializer = MobilSerializer(instance=mobil, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@api_view(['GET'])
def deleteMobil(request, pk):
  mobil = Mobil.objects.get(id=pk)
  mobil.delete()
  return Response('Data Mobil Telah di hapus')