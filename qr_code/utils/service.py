from django.http import JsonResponse
from rest_framework import status

def create_response(message=None, data=None, status_code=None):
    if message is None:
        message = ""
    if data is None:
        data = ""
    if status_code is None:
        status_code = status.HTTP_400_BAD_REQUEST
    response_content = {
        "message": message,
        "data": data
    }
    return JsonResponse(response_content, status=status_code)