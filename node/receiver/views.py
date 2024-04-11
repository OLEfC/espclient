from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def esp_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Тут ви можете обробити дані, які ви отримали від ESP32
        print(data)
        return JsonResponse({"message": "Дані успішно отримано"})
    else:
        return JsonResponse({"error": "Тільки POST запити дозволені"})
