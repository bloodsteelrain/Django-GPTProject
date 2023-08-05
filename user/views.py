from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from chatbot.models import Conversation
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
class RegisterationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            profile = Profile.objects.create(user=user)
            conversation = Conversation.objects.create(
                user=user, prompt="너(assistant)의 역할은 뭐야?",
                response="assistant는 다양한 장르에 대한 지식과 이해를 기반으로 보조 작가 역할을 수행하는 소설가이다.")
            response_data = {
                'message': '회원가입에 성공하였습니다.',
                'user': serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': '로그인에 성공하였습니다.'
            }, status=status.HTTP_200_OK)
        return Response({'error': '로그인에 실패하였습니다.'}, status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class ProfileEditView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
