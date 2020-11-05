from rest_framework import serializers 
from tileTask.models import tile,task

class TileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = tile
        fields = ('lunchDate','status')
        
        
class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = task
        fields = ('title','orderField','description','tileType','tileID')