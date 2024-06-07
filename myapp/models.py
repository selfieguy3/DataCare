from django.db import models

class Child(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    average_cost = models.DecimalField(max_digits=10, decimal_places=2)

class HealthRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    immunizations = models.TextField()
    medical_conditions = models.TextField()

class EmergencyContact(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=50)

class Allergy(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    allergy_name = models.CharField(max_length=100)
    description = models.TextField()
