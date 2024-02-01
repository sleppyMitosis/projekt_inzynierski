from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from rest_framework.authtoken.models import Token

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.urls import reverse

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'User logged in',
                'token': token.key
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'User logged out'}, status=status.HTTP_200_OK)


class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        phone_number = request.data.get('phone_number', None)
        vet_phone_number = request.data.get('vet_phone_number', None)

        if not all([username, password, email]):
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                        last_name=last_name)
        UserProfile.objects.create(user=user, phone_number=phone_number, vet_phone_number=vet_phone_number)

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'message': 'User created successfully',
            'token': token.key
        }, status=status.HTTP_201_CREATED)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            user_profile = UserProfile.objects.get(user=user)
            return Response({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'phone_number': user_profile.phone_number,
                'vet_phone_number': user_profile.vet_phone_number
            }, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile does not exist"}, status=status.HTTP_404_NOT_FOUND)


class EditUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        username = request.data.get('username')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        vet_phone_number = request.data.get('vet_phone_number')


        if username:
            user.username = username
        if email:
            user.email = email
        user.save()


        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if phone_number is not None:
            user_profile.phone_number = phone_number
        if vet_phone_number is not None:
            user_profile.vet_phone_number = vet_phone_number
        user_profile.save()

        return Response({"message": "User profile updated successfully"}, status=status.HTTP_200_OK)


class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        try:
            user.delete()
            Token.objects.filter(user=user).delete()
            return Response({"message": "User and associated data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def send_reset_email(user, request):
    token_generator = PasswordResetTokenGenerator()
    token = token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    link = f'http://localhost:3000/edit-password/{uid}/{token}'

    context = {'link': link}
    html_content = render_to_string('reset_password.html', context)

    email = EmailMessage(
        'Reset hasła',
        html_content,
        'test@example.com',
        [user.email]
    )
    email.content_subtype = 'html'
    email.send(fail_silently=False)

class PasswordResetRequestView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username', None)

        if username:
            user = User.objects.filter(email=email, username=username).first()
        else:
            user = User.objects.filter(email=email).first()

        if user:
            send_reset_email(user, request)
            return Response({'message': 'Password reset link sent to your email'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class PasswordResetConfirmView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, uidb64, token):
        print("UID:", uidb64, "Token:", token)

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as e:
            print("Error decoding UID or finding user:", e)
            return Response({'error': 'Invalid link'}, status=status.HTTP_400_BAD_REQUEST)

        if user is not None and PasswordResetTokenGenerator().check_token(user, token):
            new_password = request.data.get('password')
            print("New Password:", new_password)

            user.set_password(new_password)
            user.save()
            print("Password for user", user.username, "has been reset.")
            return Response({'message': 'Password has been reset successfully'}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid token or user ID'}, status=status.HTTP_400_BAD_REQUEST)
