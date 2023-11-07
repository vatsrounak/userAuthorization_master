from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
import firebase_admin
from firebase_admin import auth

# Initialize the Firebase Admin SDK with your serviceAccountKey.json
# Make sure to replace 'path/to/serviceAccountKey.json' with the actual path to your serviceAccountKey.json file.
# Also, ensure that the Firebase Admin SDK is correctly installed in your project.
firebase_admin.initialize_app(firebase_admin.credentials.Certificate('/home/vats/Projects/wyse_project/serviceAccountKey.json'))

User = get_user_model()

class RegistrationView(APIView):
    def post(self, request):
        # Validate and create a new user
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Create a Firebase user
            try:
                firebase_user = auth.create_user(
                    uid=str(user.id),  # Set a unique identifier for the user, e.g., user's ID
                    email=user.email,
                    password=request.data.get('password')
                )

                # Generate a custom token for the user
                custom_token = auth.create_custom_token(firebase_user.uid)

                # Return the custom token in the response
                return Response({"custom_token": custom_token}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomLoginView(APIView):
    def post(self, request):
        # Extract username and password from the request
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user using Django's built-in authentication
        user = User.objects.filter(username=username).first()

        if user is not None and user.check_password(password):
            # User is authenticated, create a Firebase user (if not already created)
            try:
                firebase_user = auth.get_user_by_email(user.email)
            except auth.AuthError as e:
                # User doesn't exist in Firebase, create a new user
                firebase_user = auth.create_user(
                    uid=str(user.id),  # Set a unique identifier for the user, e.g., user's ID
                    email=user.email,
                    password=password
                )

            # Generate a custom token for the user
            custom_token = auth.create_custom_token(firebase_user.uid)

            # Return the custom token in the response
            return Response({"custom_token": custom_token, "username": user.username}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    def get(self, request):
        # Verify the custom_token for authentication
        custom_token = request.META.get("HTTP_CUSTOM_TOKEN")
        if not custom_token:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            # Use Firebase SDK to verify the custom token
            # You should have initialized Firebase Admin SDK as previously explained
            decoded_token = auth.verify_id_token(custom_token)
            user_id = decoded_token.get("uid")

            # Retrieve the user's profile from your database
            user_profile = UserProfile.objects.get(user_id=user_id)

            # Serialize the user profile data
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        # Verify the custom_token for authentication
        custom_token = request.META.get("HTTP_CUSTOM_TOKEN")
        if not custom_token:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            # Use Firebase SDK to verify the custom token
            # You should have initialized Firebase Admin SDK as previously explained
            decoded_token = auth.verify_id_token(custom_token)
            user_id = decoded_token.get("uid")

            # Retrieve the user's profile from your database
            user_profile = UserProfile.objects.get(user_id=user_id)

            # Update user profile data based on request data
            serializer = UserProfileSerializer(user_profile, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
