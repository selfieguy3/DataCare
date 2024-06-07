from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChildForm, HealthRecordForm, EmergencyContactForm, AllergyForm
from .models import Child, HealthRecord, EmergencyContact, Allergy

def home(request):
    return render(request, 'home.html')

def child_enrollment(request):
    return render(request, 'child_enrollment.html')

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