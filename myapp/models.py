from django.db import models
from datetime import date, datetime

class Child(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    def get_age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

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
    
class Payment(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateField()

    def __str__(self):
        return f"Payment by {self.parent} on {self.payment_date}"
    
class OtherExpenses(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name

class ChildExpense(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Expense on {self.date} for {self.amount}"

class ActivityExpense(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Expense on {self.date} for {self.amount}"