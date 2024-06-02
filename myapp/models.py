# myapp/models.py
from django.db import models

class Person(models.Model):
    P_ID = models.AutoField(primary_key=True)
    P_FName = models.CharField(max_length=50)
    P_MName = models.CharField(max_length=50, blank=True, null=True)
    P_LName = models.CharField(max_length=50)
    Age = models.IntegerField()
    Person_Type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.P_FName} {self.P_LName}"
