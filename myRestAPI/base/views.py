from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
import json
import string
import random

@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    try:
        havePassword = request.data['password']
    except:
        request.data['password'] = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)))    

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)