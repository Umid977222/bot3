import http
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from rest_framework.views import APIView
from .serializer import TaskSerializer
# Create your views here.
""" /listoftask
 /addtask = create task = post
 /removetask = delete
 /updatetask  = put
 /donetask = Task.objects.filter(completed == TRUE)
 /upcommingtask = Task.objects.filter(completed == FALSE)
 """


class TaskList(APIView):
    """get_all  and post functions"""
    def getAll(self, request, format=None):
        """function get_all to convert the data in the database to json format"""
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """"""
        serializer = TaskSerializer(request=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    """put and delete functions"""
    def get_object(self, pk):
        task: Task = Task.objects.get(pk)
        try:
            return task
        except Task.DoesNotExist:
            raise status.HTTP_400_BAD_REQUEST

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        result = self.get_object(pk)
        serializer = TaskSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   def delte(self, request, pk, format=None):
        result = self.get_oject(pk)
        serializer = TaskSerializer(result, data=request.data)
        if serializer.is_valid():
            snippet.delete()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
