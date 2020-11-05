from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from tileTask.models import tile, task
from tileTask.serializers import TileSerializer, TaskSerializer
from rest_framework.decorators import api_view


def home(request):
    return render("done")

@api_view(['GET', 'POST', 'DELETE'])
def tiles_list(request):
    # GET list of tasks, POST a new tasks, DELETE all tasks
    if request.method == 'GET':
        tiles = tile.objects.all()
        tiles_serializer = TileSerializer(tiles, many=True)
        return JsonResponse(tiles_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        tile_data = JSONParser().parse(request)
        tile_serializer = TileSerializer(data=tile_data)
        if tile_serializer.is_valid():
            tile_serializer.save()
            return JsonResponse(tile_serializer.data, status=status.HTTP_201_CREATED) 
        print(tile_serializer.errors)
        return JsonResponse(tile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = tile.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def tasks_list(request):
    # GET list of tasks, POST a new tasks, DELETE all tasks
    if request.method == 'GET':
        tasks = task.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tasks = task.objects.filter(title__icontains=title)
        
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = task.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def tile_detail(request, pk):
    # find Tiles by pk (id)
    try: 
        tile_record = tile.objects.get(pk=pk) 
    except: 
        return JsonResponse({'message': 'The tile does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        tile_serializer = TileSerializer(tile_record) 
        return JsonResponse(tile_serializer.data)
    elif request.method == 'PUT': 
        tile_data = JSONParser().parse(request) 
        tile_serializer = TileSerializer(tile_record, data=tile_data) 
        if tile_serializer.is_valid(): 
            tile_serializer.save() 
            return JsonResponse(tile_serializer.data) 
        return JsonResponse(tile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        tile_record.delete() 
        return JsonResponse({'message': 'Tile was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    # GET / PUT / DELETE Tiles
    
@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    # find tasks by pk (id)
    try: 
        print(pk)
        task_record = task.objects.get(pk=pk) 
    except: 
        return JsonResponse({'message': 'The task does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        task_serializer = TaskSerializer(task_record) 
        return JsonResponse(task_serializer.data)
    elif request.method == 'PUT': 
        task_data = JSONParser().parse(request) 
        task_serializer = TaskSerializer(task_record, data=task_data) 
        if task_serializer.is_valid(): 
            task_serializer.save() 
            return JsonResponse(task_serializer.data) 
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        task_record.delete() 
        return JsonResponse({'message': 'Task was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    # GET / PUT / DELETE Tasks    
