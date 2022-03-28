from rest_framework.response import Response
from .models import UserDetails
from .serializers import UserDetailsSerializers
from rest_framework import status
from rest_framework.views import APIView


class UserApi(APIView):

    def post(self, request):
        serializer = UserDetailsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User Created'}, status=status.
                            HTTP_201_CREATED)

        return Response(serializer.errors, status=status.
                        HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        id = pk
        user_instance = UserDetails.objects.get(pk=id)
        user_instance.delete()
        return Response({'msg': 'Data deleted'})
