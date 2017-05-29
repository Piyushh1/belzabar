
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
import sys
import pdb

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer  # in generics.py we have 2 variables serializer_class, query set so we need to override that variables with this  value
                                       # thats why after overriding value of query set , we dont need to pass arguments of query sert in User Serializer , as value of qeury set is laready updated in geenerics.py
                                      #  so all the function of create update in mixins we get the value
#
# @api_view(['GET', 'POST'])
# def user_list(request):
#     """
#     List all Users, or create a new User.
#     """
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         pdb.set_trace()
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail(request, pk):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = UserSerializer(user, data=request.data) #in PUT write the old data use and the new data to update
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
