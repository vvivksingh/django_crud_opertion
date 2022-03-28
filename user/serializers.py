from rest_framework import serializers
from .models import UserDetails


class UserDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['name', 'address', 'city', 'state', 'mobile_no']
