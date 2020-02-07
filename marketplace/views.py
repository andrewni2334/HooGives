from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import uuid
# Create your views here.
from django.shortcuts import render,redirect
from .models import User, Event
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

@csrf_exempt
def user_api(request):
    some_data_to_dump = {}
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            uuid.UUID(str(user_id))
            if user_id:
                if User.objects.filter(pk = user_id).count() != 0:
                    user = User.objects.get(pk = user_id )
                    
                    first_name = request.POST.get('first_name')
                    if first_name:
                        user.first_name = first_name
                    last_name = request.POST.get('last_name')
                    if last_name:
                        user.last_name = last_name

                    phone_number = request.POST.get("phone_number")
                    if phone_number:
                        user.phone_number = phone_number
                    
                    email = request.POST.get("email")
                    if email:
                        user.email = email

                    user.save()
                    some_data_to_dump = model_to_dict(user)
                else:
                    some_data_to_dump["Error:"] = "Invalid User ID: no user found to update"
        except ValueError:
            some_data_to_dump["Error:"] = "Invalid User ID: no user found to retrieve info"

    if request.method == "GET":
        user_id = request.GET.get('user_id')
        try:
            uuid.UUID(str(user_id))
            if user_id:
                    user = User.objects.get(pk = user_id )
                    some_data_to_dump = model_to_dict(user)
            else:
                    some_data_to_dump["Error:"] = "Invalid User ID: no user found to retrieve info"
        except ValueError:
            some_data_to_dump["Error:"] = "Invalid User ID: no user found to retrieve info"
       
            
    return JsonResponse(some_data_to_dump)

