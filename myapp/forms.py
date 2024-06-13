from django import forms
from .models import ActivityExpense, Child, ChildExpense, HealthRecord, EmergencyContact, Allergy, Parent, ParentChildRelationship, Staff, Activity, StaffChildAssignment, StaffActivityAssignment, ChildActivityAssignment, Attendance, Payment, OtherExpenses

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'middle_name', 'last_name', 'date_of_birth']

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['child', 'immunizations', 'medical_conditions']

class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ['child', 'first_name', 'middle_name', 'last_name', 'phone_number', 'street_address', 'city', 'zip_code', 'state']

class AllergyForm(forms.ModelForm):
    class Meta:
        model = Allergy
        fields = ['child', 'allergy_name', 'description']

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['first_name', 'middle_name', 'last_name', 'age', 'phone_number', 'street_address', 'city', 'zip_code', 'state', 'email']


class ParentChildRelationshipForm(forms.ModelForm):
    class Meta:
        model = ParentChildRelationship
        fields = ['parent', 'child']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'middle_name', 'last_name', 'age', 'phone_number', 'street_address', 'city', 'zip_code', 'state', 'email']

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_name', 'duration', 'cost', 'age_group', 'description']

class StaffChildAssignmentForm(forms.ModelForm):
    class Meta:
        model = StaffChildAssignment
        fields = ['staff', 'child', 'date']

class StaffActivityAssignmentForm(forms.ModelForm):
    class Meta:
        model = StaffActivityAssignment
        fields = ['staff', 'activity', 'date']

class ChildActivityAssignmentForm(forms.ModelForm):
    class Meta:
        model = ChildActivityAssignment
        fields = ['child', 'activity', 'date']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['date', 'child', 'is_present']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'is_present': forms.CheckboxInput()
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['parent', 'amount_paid', 'payment_method', 'payment_date']
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ChildExpenseForm(forms.ModelForm):
    class Meta:
        model = ChildExpense
        fields = ['child', 'date', 'amount', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        
class ActivityExpenseForm(forms.ModelForm):
    class Meta:
        model = ActivityExpense
        fields = ['activity', 'date', 'amount', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class OtherExpensesForm(forms.ModelForm):
    class Meta:
        model = OtherExpenses
        fields = ['name', 'cost', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

