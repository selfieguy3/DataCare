from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChildForm, HealthRecordForm, EmergencyContactForm, AllergyForm, ParentForm, ParentChildRelationshipForm
from .models import Child, HealthRecord, EmergencyContact, Allergy, Parent, ParentChildRelationship

def home(request):
    return render(request, 'home.html')

def child_enrollment(request):
    context = {
        'children': Child.objects.all(), 
        'health_records': HealthRecord.objects.all(), 
        'emergency_contacts': EmergencyContact.objects.all(), 
        'allergies': Allergy.objects.all(), 
    }
    return render(request, 'child_enrollment.html', context)

def add_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('child_enrollment')
    else:
        form = ChildForm()
    return render(request, 'add_child.html', {'form': form})

def edit_child(request, pk):
    child = get_object_or_404(Child, pk=pk)
    if request.method == 'POST':
        form = ChildForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            return redirect('child_enrollment')
    else:
        form = ChildForm(instance=child)
    return render(request, 'edit_child.html', {'form': form})

def delete_child(request, pk):
    child = get_object_or_404(Child, pk=pk)
    if request.method == 'POST':
        child.delete()
        return redirect('child_enrollment')
    return render(request, 'confirm_delete.html', {'object': child})

def add_health_record(request):
    if request.method == 'POST':
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('child_enrollment')
    else:
        form = HealthRecordForm()
    return render(request, 'add_health_record.html', {'form': form})

def edit_health_record(request, pk):
    record = get_object_or_404(HealthRecord, pk=pk)
    if request.method == 'POST':
        form = HealthRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('child_enrollment')
    else:
        form = HealthRecordForm(instance=record)
    return render(request, 'edit_health_record.html', {'form': form})

def delete_health_record(request, pk):
    record = get_object_or_404(HealthRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('child_enrollment')
    return render(request, 'confirm_delete.html', {'object': record})

def add_emergency_contact(request):
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('child_enrollment')
    else:
        form = EmergencyContactForm()
    return render(request, 'add_emergency_contact.html', {'form': form})

def edit_emergency_contact(request, pk):
    contact = get_object_or_404(EmergencyContact, pk=pk)
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('child_enrollment')
    else:
        form = EmergencyContactForm(instance=contact)
    return render(request, 'edit_emergency_contact.html', {'form': form})

def delete_emergency_contact(request, pk):
    contact = get_object_or_404(EmergencyContact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('child_enrollment')
    return render(request, 'confirm_delete.html', {'object': contact})

def add_allergy(request):
    if request.method == 'POST':
        form = AllergyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('child_enrollment')
    else:
        form = AllergyForm()
    return render(request, 'add_allergy.html', {'form': form})

def edit_allergy(request, pk):
    allergy = get_object_or_404(Allergy, pk=pk)
    if request.method == 'POST':
        form = AllergyForm(request.POST, instance=allergy)
        if form.is_valid():
            form.save()
            return redirect('child_enrollment')
    else:
        form = AllergyForm(instance=allergy)
    return render(request, 'edit_allergy.html', {'form': form})

def delete_allergy(request, pk):
    allergy = get_object_or_404(Allergy, pk=pk)
    if request.method == 'POST':
        allergy.delete()
        return redirect('child_enrollment')
    return render(request, 'confirm_delete.html', {'object': allergy})


def parent_list(request):
    parents = Parent.objects.all()
    relationships = ParentChildRelationship.objects.all()
    return render(request, 'parent_list.html', {'parents': parents, 
                                                'relationships': relationships})

def add_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parent_list')
    else:
        form = ParentForm()
    return render(request, 'add_parents.html', {'form': form})


def edit_parent(request, parent_id):
    parent = get_object_or_404(Parent, id=parent_id)
    if request.method == 'POST':
        form = ParentForm(request.POST, instance=parent)
        if form.is_valid():
            form.save()
            return redirect('parent_list')
    else:
        form = ParentForm(instance=parent)
    return render(request, 'edit_parents.html', {'form': form})


def delete_parent(request, parent_id):
    parent = get_object_or_404(Parent, id=parent_id)
    if request.method == 'POST':
        parent.delete()
        return redirect('parent_list')
    return render(request, 'confirm_delete1.html', {'object': parent})


def assign_child(request):
    if request.method == 'POST':
        form = ParentChildRelationshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parent_list')
    else:
        form = ParentChildRelationshipForm()
    return render(request, 'assign_child.html', {'form': form})


def edit_relationship(request, relationship_id):
    relationship = get_object_or_404(ParentChildRelationship, id=relationship_id)
    if request.method == 'POST':
        form = ParentChildRelationshipForm(request.POST, instance=relationship)
        if form.is_valid():
            form.save()
            return redirect('parent_list')
    else:
        form = ParentChildRelationshipForm(instance=relationship)
    return render(request, 'edit_relationship.html', {'form': form})


def delete_relationship(request, relationship_id):
    relationship = get_object_or_404(ParentChildRelationship, id=relationship_id)
    relationship.delete()
    return redirect('parent_list')

