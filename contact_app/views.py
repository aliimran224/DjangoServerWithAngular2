from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Contact
from .serializers import CustomerSerializer
from rest_framework import status
from django.http import Http404


class ContactListView(APIView):


    def get(self, *args):
        contact = Contact.objects.all()
        serializer = CustomerSerializer(contact, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"serializer.data": 200, "status": status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetail(APIView):

    def get_object(self, id):
        try:
            return Contact.objects.get(id=id)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        contact = self.get_object(id)
        serializer = CustomerSerializer(contact)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        contact = self.get_object(id)
        serializer = CustomerSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        contact = self.get_object(id)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





