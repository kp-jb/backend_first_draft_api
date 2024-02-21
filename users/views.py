from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomUserSerializer


class CreateCustomUserView(APIView):
    # Anyone can register!
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

