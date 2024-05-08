from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate

class RegisterView(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'message': serializer.errors,
                    'data': {}
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response({'message': "Successfully registered"}, status=status.HTTP_201_CREATED)
        except Exception as e:

            return Response({'message': 'An Error has occurred while registering user', 'data': {}}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):

        data = request.data
        serializer = LoginSerializer(data=data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)

            if not user:
                return Response({'message': 'User has not logged in'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'User has successfully logged in'},status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_200_OK)