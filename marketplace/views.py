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


@csrf_exempt
def event_api(request):
    some_data_to_dump = {}
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        try:
            uuid.UUID(str(event_id))
            if event_id:
                if Event.objects.filter(pk = event_id).count() != 0:
                    event = Event.objects.get(pk = event_id )
                    
                    event_name = request.POST.get('event_name')
                    if event_name:
                        event.event_name = event_name
                    event_date = request.POST.get('event_date')
                    if event_date:
                        event.event_date = event_date

                    event_description = request.POST.get("event_description")
                    if event_description:
                        event.event_description = event_description
                    
                   
                    event.save()
                    some_data_to_dump = model_to_dict(event)
                else:
                    some_data_to_dump["Error:"] = "Invalid Event ID: no event found to update"
        except ValueError:
            some_data_to_dump["Error:"] = "Invalid Event ID: no event found to retrieve info"

    if request.method == "GET":
        event_id = request.GET.get('event_id')
        try:
            uuid.UUID(str(event_id))
            if event_id:
                    event = Event.objects.get(pk = event_id )
                    some_data_to_dump = model_to_dict(event)
            else:
                    some_data_to_dump["Error:"] = "Invalid Event ID: no event found to retrieve info"
        except ValueError:
            some_data_to_dump["Error:"] = "Invalid Event ID: no user found to retrieve info"
       
            
    return JsonResponse(some_data_to_dump)

@csrf_exempt
def event_create_api(request):
    some_data_to_dump = {}
    if request.method == 'POST':     
        try:
            event_name = request.POST.get('event_name')      
            event_date = request.POST.get('event_date')            
            event_description = request.POST.get("event_description")            
            some_data_to_dump["values"] = [event_name , event_date , event_description]

            if(event_name and event_date and event_description):
                event = Event.objects.create(
                    event_name = event_name,
                    event_date = event_date,
                    event_description = event_description
                )
                event.save()
                some_data_to_dump = model_to_dict(event)
            else:
                some_data_to_dump["Error:"] = "not all event parameters specified"

        except ValueError:
            some_data_to_dump["Error:"] = "creation failed"  
    else:
        some_data_to_dump["Error:"] = "Invalid method: POST only"

    return JsonResponse(some_data_to_dump)

@csrf_exempt
def event_delete_api(request):
    some_data_to_dump = {}
    if request.method == "GET":
        try:
            event_id = request.GET.get('event_id')
            uuid.UUID(str(event_id))
            if event_id:
                if Event.objects.filter(pk = event_id).count() != 0:
                    event = Event.objects.get(pk = event_id )                 
                    some_data_to_dump = model_to_dict(event)
                    some_data_to_dump["event succesfully deleted"] = True
                    event.delete()                
                else:
                    some_data_to_dump["Error:"] = "Invalid Event ID: no event found to delete"
        except ValueError:
            some_data_to_dump["Error:"] = "Invalid Event ID: no event found to delete"
         
    return JsonResponse(some_data_to_dump)

