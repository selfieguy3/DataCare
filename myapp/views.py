from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChildForm, HealthRecordForm, EmergencyContactForm, AllergyForm, ParentForm, ParentChildRelationshipForm, StaffForm, ActivityForm, StaffChildAssignmentForm, StaffActivityAssignmentForm, ChildActivityAssignmentForm, AttendanceForm, PaymentForm, ExpenseForm, OtherExpensesForm
from .models import Child, HealthRecord, EmergencyContact, Allergy, Parent, ParentChildRelationship, Staff, Activity, StaffChildAssignment, StaffActivityAssignment, ChildActivityAssignment, Attendance, Payment, Expense, OtherExpenses

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

def staff_list(request):
    staffs = Staff.objects.all()
    staff_child_assignments = StaffChildAssignment.objects.all()
    staff_activity_assignments = StaffActivityAssignment.objects.all()
    return render(request, 'staff_list.html', {
        'staffs': staffs, 
        'staff_child_assignments': staff_child_assignments,
        'staff_activity_assignments': staff_activity_assignments
    })


def staff_add(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'add_staff.html', {'form': form})


def staff_edit(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'edit_staff.html', {'form': form})

def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff_list')
    return render(request, 'confirm_delete2.html', {'staff': staff})

def assign_staff_child(request):
    if request.method == 'POST':
        form = StaffChildAssignmentForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffChildAssignmentForm()
    return render(request, 'assign_staff_child.html', {'form': form})

def edit_staff_child_assignment(request, assignment_id):
    assignment = get_object_or_404(StaffChildAssignment, pk=assignment_id)
    if request.method == 'POST':
        form = StaffChildAssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffChildAssignmentForm(instance=assignment)
    return render(request, 'edit_staff_child_assignment.html', {'form': form})

def delete_staff_child_assignment(request, assignment_id):
    assignment = get_object_or_404(StaffChildAssignment, id=assignment_id)
    assignment.delete()
    return redirect('staff_list')

def assign_staff_activity(request):
    if request.method == 'POST':
        form = StaffActivityAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffActivityAssignmentForm()
    return render(request, 'assign_staff_activity.html', {'form': form})

def edit_staff_activity_assignment(request, assignment_id):
    assignment = get_object_or_404(StaffActivityAssignment, pk=assignment_id)
    if request.method == 'POST':
        form = StaffActivityAssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffActivityAssignmentForm(instance=assignment)
    return render(request, 'edit_staff_activity_assignment.html', {'form': form})

def delete_staff_activity_assignment(request, assignment_id):
    assignment = get_object_or_404(StaffActivityAssignment, id=assignment_id)
    assignment.delete()
    return redirect('staff_list')

from django.shortcuts import render
from .models import Activity, ChildActivityAssignment

def activity_list(request):
    activities = Activity.objects.all()
    child_activities_assignments = ChildActivityAssignment.objects.all()
    return render(request, 'activity_list.html', {
        'activities': activities,
        'child_activities_assignments': child_activities_assignments
    })


def activity_add(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = ActivityForm()
    return render(request, 'add_activity.html', {'form': form})

def activity_edit(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'edit_activity.html', {'form': form})

def activity_delete(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('activity_list')
    return render(request, 'confirm_delete3.html', {'activity': activity})

def assign_activity_child(request):
    if request.method == 'POST':
        form = ChildActivityAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = ChildActivityAssignmentForm()
    return render(request, 'assign_child_activity.html', {'form': form})

def edit_activity_assignment(request, assignment_id):
    assignment = get_object_or_404(ChildActivityAssignment, pk=assignment_id)
    if request.method == 'POST':
        form = ChildActivityAssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = ChildActivityAssignmentForm(instance=assignment)
    return render(request, 'edit_activity_assignment.html', {'form': form})

def delete_activity_assignment(request, assignment_id):
    assignment = get_object_or_404(ChildActivityAssignment, id=assignment_id)
    assignment.delete()
    return redirect('activity_list')

def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'attendances': attendances})

def add_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'add_attendance.html', {'form': form})

def edit_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'edit_attendance.html', {'form': form})

def delete_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        attendance.delete()
        return redirect('attendance_list')
    return render(request, 'confirm_delete4.html', {'object': attendance})

def payment_list(request):
    payments = Payment.objects.all()
    expenses = Expense.objects.all()
    other_expenses = OtherExpenses.objects.all()
    return render(request, 'payment_list.html', {'payments': payments,
                                                 'expenses': expenses,
                                                 'other_expenses': other_expenses})

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'add_payment.html', {'form': form})

def edit_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'edit_payment.html', {'form': form})

def delete_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        payment.delete()
        return redirect('payment_list')
    return render(request, 'confirm_delete5.html', {'object': payment})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'edit_expense.html', {'form': form})

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('payment_list')
    return render(request, 'confirm_delete6.html', {'object': expense})

def add_other_expense(request):
    if request.method == 'POST':
        form = OtherExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = OtherExpensesForm()
    return render(request, 'add_other_expense.html', {'form': form})

def edit_other_expense(request, pk):
    other_expense = get_object_or_404(OtherExpenses, pk=pk)
    if request.method == 'POST':
        form = OtherExpensesForm(request.POST, instance=other_expense)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = OtherExpensesForm(instance=other_expense)
    return render(request, 'edit_other_expense.html', {'form': form})

def delete_other_expense(request, pk):
    other_expense = get_object_or_404(OtherExpenses, pk=pk)
    if request.method == 'POST':
        other_expense.delete()
        return redirect('payment_list')
    return render(request, 'confirm_delete7.html', {'object': other_expense})