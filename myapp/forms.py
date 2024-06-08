from django import forms
from .models import Child, HealthRecord, EmergencyContact, Allergy, Parent, ParentChildRelationship, Staff, Activity, StaffChildAssignment, StaffActivityAssignment

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'middle_name', 'last_name', 'age', 'date_of_birth', 'average_cost']

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
        fields = ['first_name', 'middle_name', 'last_name', 'age', 'salary', 'phone_number', 'street_address', 'city', 'zip_code', 'state', 'email']

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
