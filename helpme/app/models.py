from django.db import models
from django.contrib.auth.models import User
from datetime import date, timezone, timedelta

# Create your models here.
class Venue(models.Model):
    name = models.CharField("Venue Name", max_length=255, null=True)
    floor = models.IntegerField("Floor", null=True)
    
    def __str__(self):
        return self.name + " | " + self.floor
    

class Team(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField("Team Name", max_length=255, null=True)
    tableNumber = models.IntegerField("Table Number", null=True)
    venue = models.ForeignKey(Venue, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.tableNumber + " | " + self.name
    

class Ticket(models.Model):
    STATUS = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Accepted', 'Accepted'),
    )

    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    desc = models.CharField("Issue Description", max_length=255, null=True)
    platform = models.CharField("Platform Information", max_length=255, null=True)
    status = models.CharField("Status", max_length=255, choices=STATUS, default='Open', null=True)
    timeCreated = models.DateTimeField("Created Time", auto_now_add=True)
    timeClosed = models.DateTimeField("Closed Time", auto_now_add=True)
    
    def __str__(self):
        return self.user.team.tableNumber + " | " + self.team.name + " | " + self.timeCreated + " | " + self.status