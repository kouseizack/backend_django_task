from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
from .models import User , Activity_Periods

def index(request):
    return HttpResponse("You have entered the main page")

def delete_data(request):
        User.objects.all().delete()
        Activity_Periods.objects.all().delete()
        return HttpResponse("All tables deleted")

def show_data(request):
        return render(request , "json_api/index.html",{
                "users" : User.objects.all(), "time" : Activity_Periods.objects.all()
        }) 

def add_data(request):
    if(request.method == 'POST'):
        received_json_data = json.loads(request.body)
        members = received_json_data["members"]
        #print (members)
        for member in members:
                given_id = member['id']
                real_name = member['real_name']
                time_zone = member["tz"]
                print (given_id , real_name , time_zone) 
                activity_periods = member["activity_periods"]
                if(not User.objects.filter(given_id = given_id).exists()):
                        user = User(given_id = given_id , real_name = real_name , time_zone = time_zone)
                        user.save()
                else:
                        user = User.objects.filter(given_id = given_id).first()
                for activity_period in activity_periods:
                        time_period = Activity_Periods(start_time = activity_period["start_time"] , end_time = activity_period["end_time"] , user_id = user)
                        time_period.save()
        return HttpResponse(f"Data entered : {str(received_json_data)}")

    
