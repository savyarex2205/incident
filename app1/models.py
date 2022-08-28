from django.db import models
from django.utils import timezone
# from datetime import datetime

class Users(models.Model):
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    userID = models.IntegerField(auto_created=True, null=False, primary_key=True, unique=True)

    def __str__(self):
        return self.userName

class Incidents(models.Model):
    incidentID = models.CharField(max_length=12, unique=True, primary_key=True)
    reportName = models.ForeignKey(Users, null=False, on_delete=models.CASCADE)
    incidentDetails = models.CharField(max_length=100)
    incidentDateTime = models.DateTimeField(default=timezone.now)
    incidentPriority = models.IntegerField(default=0)
    incidentStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.incidentID
