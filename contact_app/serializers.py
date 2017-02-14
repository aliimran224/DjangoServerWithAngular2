from .models import *
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ("id", "name", "phone","suite","city", "street", "email", "zipcode")

