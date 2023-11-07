from firebase_admin import auth
from rest_framework import status
from django.http import JsonResponse

class FirebaseTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        custom_token = request.META.get("HTTP_CUSTOM_TOKEN")

        if not custom_token:
            return JsonResponse({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            decoded_token = auth.verify_id_token(custom_token)
            request.firebase_user_id = decoded_token.get("uid")
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        response = self.get_response(request)
        return response
