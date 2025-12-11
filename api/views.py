# api/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
import json
from .services import create_user, get_user, update_user, delete_user
from .serializers import UserSerializer
from django.core.exceptions import ObjectDoesNotExist

@csrf_exempt
@require_http_methods(["POST"])
def create_user_view(request):
    data = json.loads(request.body)
    user = create_user(data['username'], data['email'])
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data, status=201)

@csrf_exempt
@require_http_methods(["GET"])
def get_user_view(request, user_id):
    try:
        user = get_user(user_id)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

@csrf_exempt
@require_http_methods(["PUT"])
def update_user_view(request, user_id):
    try:
        data = json.loads(request.body)
        user = update_user(
            user_id,
            username=data.get('username'),
            email=data.get('email')
        )
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_user_view(request, user_id):
    success = delete_user(user_id)
    if success:
        return JsonResponse({"message": "User deleted"}, status=200)
    else:
        return JsonResponse({"error": "User not found"}, status=404)