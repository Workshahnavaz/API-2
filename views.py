from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import *
from.serializers import *

@api_view(['GET'])
def vehical(request):
    m = turiste.objects.all()
    u = turistserializer(m,many=True)
    return Response({"status" : 200, "Loading" : u.data})

@api_view(['GET'])
def vehical2(request):
    y = visitor.objects.all()
    f = visitorserializer(y,many = True)
    return Response({"status" : 200, "Loading" : f.data, "show" : "compleated"})


