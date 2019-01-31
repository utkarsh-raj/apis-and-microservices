from django.shortcuts import render
from exerciseTracker.models import ExerciseUser, Exercise
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import timestring

# Create your views here.

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        username = request.POST["username"]

        user = ExerciseUser(name = username)

        user.save()

        print(user)

        return JsonResponse({
            "username": username,
            "id": user.id
        })

@csrf_exempt
def create_exercise(request):
    if request.method == "POST":
        date = ""

        try:
            id = request.POST["id"]
            description = request.POST["description"]
            duration = request.POST["duration"]
            date = request.POST["date"]
        except:
            if date == "":
                date = datetime.now()

        user_instance = ExerciseUser.objects.get(id = id)

        exercise = Exercise(user = user_instance, description = description, duration = duration, date = date)

        exercise.save()

        return JsonResponse({
            "username": user_instance.name,
            "_id": user_instance.id,
            "description": exercise.description,
            "duration": exercise.duration,
            "date": exercise.date
        })

def get_description(request):
    from_date = ""
    to_date = ""
    limit = ""
    try:
        id = request.GET["userId"]
    except:
        pass
    try:
        from_date = request.GET["from"]
    except:
        pass
    try:
        to_date = request.GET["to"]
    except:
        pass
    try:
        limit = request.GET["limit"]
    except:
        pass

    user_instance = ExerciseUser.objects.get(id = id)
    exercises = Exercise.objects.filter(user = user_instance)
    log = []
    if from_date == "":
        if limit == "":
            for exercise in exercises:
                temp = {
                    "description": exercise.description,
                    "date": exercise.date,
                    "duration": exercise.duration
                }
                log.append(temp)
            print(log)
            print("first")
            if len(log) == 0:
                start = from_date
                finish = to_date
            else:
                start = log[0]["date"]
                finish = log[-1]["date"]
            return JsonResponse({
                "_id": user_instance.id,
                "username": user_instance.name,
                "from": start,
                "to": finish,
                "count": len(log),
                "log": log
            }) 
        else:
            for exercise in exercises:
                temp = {
                    "description": exercise.description,
                    "date": exercise.date,
                    "duration": exercise.duration
                }
                log.append(temp)
            log = log[ : int(limit)]
            print(log)
            if len(log) == 0:
                start = from_date
                finish = to_date
            else:
                start = log[0]["date"]
                finish = log[-1]["date"]
            return JsonResponse({
                "_id": user_instance.id,
                "username": user_instance.name,
                "from": start,
                "to": finish,
                "count": len(log),
                "log": log
            })
    else:
        for exercise in exercises:
            if exercise.date >= timestring.Date(from_date) and exercise.date <= timestring.Date(to_date):
                temp = {
                    "description": exercise.description,
                    "date": exercise.date,
                    "duration": exercise.duration
                }
                log.append(temp)
        if len(log) == 0:
                start = from_date
                finish = to_date
        else:
            start = log[0]["date"]
            finish = log[-1]["date"]
        return JsonResponse({
            "_id": user_instance.id,
            "username": user_instance.name,
            "from": start,
            "to": finish,
            "count": len(log),
            "log": log
        })

def get_users(request):
    userList = ExerciseUser.objects.all()

    responseList = {}

    for user in userList:
        responseList.update({
            "username": user.name,
            "_id": user.id
        })
    return JsonResponse(responseList)