from django import forms
from .models import Child, HealthRecord, EmergencyContact, Allergy, Parent, ParentChildRelationship

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
