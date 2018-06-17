from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import TodoSerializer
from .models import Todo
# Create your views here.


@csrf_exempt
def ref_task_list(request):
    if request.method == "GET":
        todo_list = Todo.objects.all()
        todo_serializer = TodoSerializer(todo_list, many=True)
        return JsonResponse(todo_serializer.data, safe=False)


@csrf_exempt
def create_task(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        user = User.objects.filter(username=data["user_id"])[0]
        data["user"] = user.id

        todo_serializer = TodoSerializer(data=data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse(todo_serializer.data, status=201)

        return JsonResponse(todo_serializer.errors, status=400)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        print(data)
        todo = Todo.objects.filter(id=data["id"])[0]
        todo.contents = data["contents"]
        data["user"] = todo.user.id
        todo_serializer = TodoSerializer(todo, data=data)

        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse(todo_serializer.data, status=201)
        return JsonResponse(todo_serializer.errors, status=400)

    elif request.method == "DELETE":
        data = JSONParser().parse(request)
        Todo.objects.filter(id=data["id"])[0].delete()
        return JsonResponse(data={}, status=status.HTTP_204_NO_CONTENT)


