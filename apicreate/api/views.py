from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import  Response
from .serializer import UserSerilaizer
from .models import UserDetails
# Create your views here.

@api_view(['GET'])
def getUser(request):
    users=UserDetails.objects.all()
    serializer=UserSerilaizer(users,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def create_user(request):
    serializer=UserSerilaizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])
def update_user(request,id):
    try:
        user=UserDetails.objects.get(id=id)
    except UserDetails.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='GET':
        serializer=UserSerilaizer(user)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=UserSerilaizer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)