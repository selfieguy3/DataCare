from django.db import models

class Child(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    average_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name} (ID: {self.id})"

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

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name} (ID: {self.id})"

class Allergy(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    allergy_name = models.CharField(max_length=100)
    description = models.TextField()

class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name} (ID: {self.id})"


class ParentChildRelationship(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

class Staff(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name} (ID: {self.id})"

class Activity(models.Model):
    activity_name = models.CharField(max_length=50)
    duration = models.DurationField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    age_group = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f"{self.activity_name} (ID: {self.id})"

class StaffChildAssignment(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()

class StaffActivityAssignment(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date = models.DateField()

class ChildActivityAssignment(models.Model):   
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"Assigned {self.child.first_name} {self.child.middle_name} {self.child.last_name} to {self.activity.activity_name} on {self.date}"

class Attendance(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=True)

    def __str__(self):
        return f"Attendance for {self.child} on {self.date}"