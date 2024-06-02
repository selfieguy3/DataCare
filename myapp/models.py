# myapp/models.py
from django.db import models

class Person(models.Model):
    P_ID = models.AutoField(primary_key=True)
    P_FName = models.CharField(max_length=50)
    P_MName = models.CharField(max_length=50, blank=True, null=True)
    P_LName = models.CharField(max_length=50)
    Age = models.IntegerField()
    PERSON_TYPE = [
        ('staff', 'Staff'),
        ('child', 'Child'),
        ('parent', 'Parent')
    ]
    Person_Type = models.CharField(max_length=10, choices=PERSON_TYPE, default='staff')
# default is staff~

    def __str__(self):
        return f"{self.P_FName} {self.P_LName}"

class Staff(Person):
    STAFF_ID = models.AutoField(primary_key=True)
    Employee_Salary = models.DecimalField(max_digits=10, decimal_places=2)
    ZipCode = models.IntegerField()
    Phone_Number = models.CharField(max_length=15)
    Street_Address = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Email = models.EmailField()

    def __str__(self):
        return f"Staff: {self.P_FName} {self.P_LName}, Staff ID: {self.STAFF_ID}"

class Child(Person):
    CHILD_ID = models.AutoField(primary_key=True)
    HEALTH_RECORD_ID = models.IntegerField()
    Date_of_Birth = models.DateField()
    AVERAGE_COST = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Child: {self.P_FName} {self.P_LName}, Child ID: {self.CHILD_ID}"

class Parent(Person):
    PARENT_ID = models.AutoField(primary_key=True)
    Phone_Number = models.CharField(max_length=15)
    Street_Address = models.CharField(max_length=100)
    ZipCode = models.IntegerField()
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Email = models.EmailField()

    def __str__(self):
        return f"Parent: {self.P_FName} {self.P_LName}, Parent ID: {self.PARENT_ID}"

class ParentChild(models.Model):
    PARENT_ID = models.ForeignKey(Parent, on_delete=models.CASCADE)
    CHILD_ID = models.ForeignKey(Child, on_delete=models.CASCADE)

    def __str__(self):
        return f"Parent ID: {self.PARENT_ID}, Child ID: {self.CHILD_ID}"

class ChildStaff(models.Model):
    STAFF_ID = models.ForeignKey(Staff, on_delete=models.CASCADE)
    CHILD_ID = models.ForeignKey(Child, on_delete=models.CASCADE)

    def __str__(self):
        return f"Staff ID: {self.STAFF_ID}, Child ID: {self.CHILD_ID}"