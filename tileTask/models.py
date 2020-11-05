from django.utils.translation import gettext as _
from django.db import models
import datetime

# Create your models here.
class tile(models.Model):
    
    STATUS_TILE = (('live', _('live')),('pending', _('pending by someone')),('archived', _('Archived - not available anymore')),)
    
    tileID = models.AutoField(primary_key=True)
    lunchDate = models.DateField(_("Date"), default=datetime.date.today)
    status = models.CharField(max_length=200,choices=STATUS_TILE,default='live',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class task(models.Model):
    
    STATUS_TASK = (('survey', _('survey - survey description')),('discussion', _('discussion - discussion description')),('diary', _('diary - diary description')),)
    
    taskID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    orderField = models.CharField(max_length=200)
    description = models.TextField()
    tileType = models.CharField(max_length=200,choices=STATUS_TASK,default='survey',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tileID = models.ForeignKey(tile, on_delete=models.CASCADE)
    