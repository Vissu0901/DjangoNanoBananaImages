from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer, ChangePasswordSerializer, NanoBananaCardSerializer
from rest_framework import permissions, status
from .models import NanoBananaCard


class WelcomeView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        return Response({'message': 'welcome, to Nano Banana image generator'}, status=status.HTTP_200_OK)

class UserRegister(APIView):
	permission_classes = [permissions.AllowAny]
	authentication_classes = []
	def post(self, request):
		serializer = UserRegisterSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLogin(APIView):
	permission_classes = [permissions.AllowAny]
	authentication_classes = []
	def post(self, request):
		serializer = UserLoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.check_user(serializer.validated_data)
		login(request, user)
		return Response({
            'message': 'development in progress',
            'email': user.email
        }, status=status.HTTP_200_OK)


class UserLogout(APIView):
	permission_classes = [permissions.IsAuthenticated]
	authentication_classes = [SessionAuthentication]
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
	permission_classes = [permissions.IsAuthenticated]
	authentication_classes = [SessionAuthentication]
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        old_password = serializer.validated_data['old_password']
        new_password = serializer.validated_data['new_password']

        if not user.check_password(old_password):
            return Response({'detail': 'Old password is not correct.'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({'detail': 'Password updated successfully.'}, status=status.HTTP_200_OK)


class CardCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        serializer = NanoBananaCardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        cards = NanoBananaCard.objects.filter(user=request.user)
        serializer = NanoBananaCardSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
