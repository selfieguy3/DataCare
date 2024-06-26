from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Sum
from django.utils import timezone
from datetime import datetime, timedelta, date
from .forms import ChildForm, HealthRecordForm, EmergencyContactForm, AllergyForm, ParentForm, ParentChildRelationshipForm, StaffForm, ActivityForm, StaffChildAssignmentForm, StaffActivityAssignmentForm, ChildActivityAssignmentForm, AttendanceForm, PaymentForm, OtherExpensesForm, ActivityExpenseForm, ChildExpenseForm
from .models import ActivityExpense, Child, ChildExpense, HealthRecord, EmergencyContact, Allergy, Parent, ParentChildRelationship, Staff, Activity, StaffChildAssignment, StaffActivityAssignment, ChildActivityAssignment, Attendance, Payment, OtherExpenses, ChildExpense, ActivityExpense

def home(request):
    return render(request, 'home.html')

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def child_enrollment(request):
    children = Child.objects.order_by('-id')[:5] 
    children_with_age = []
    for child in children:
        child_info = {
            'id': child.id,
            'first_name': child.first_name,
            'middle_name': child.middle_name,
            'last_name': child.last_name,
            'date_of_birth': child.date_of_birth,
            'age': calculate_age(child.date_of_birth)
        }
        children_with_age.append(child_info)

    context = {
        'children': children_with_age, 
        'health_records': HealthRecord.objects.order_by('-id'), 
        'emergency_contacts': EmergencyContact.objects.order_by('-id')[:5],
        'allergies': Allergy.objects.order_by('-id')[:5],
    }
    return render(request, 'child_enrollment.html', context)

def all_children(request):
    children = Child.objects.order_by('-id')
    children_with_age = []
    for child in children:
        child_info = {
            'id': child.id,
            'first_name': child.first_name,
            'middle_name': child.middle_name,
            'last_name': child.last_name,
            'date_of_birth': child.date_of_birth,
            'age': calculate_age(child.date_of_birth)
        }
        children_with_age.append(child_info)

    return render(request, 'all_children.html', {'children': children_with_age})

def all_immunizations(request):
    health_records = HealthRecord.objects.order_by('-id')
    immunizations = []
    for record in health_records:
        child = record.child
        immunization_info = {
            'child_id': child.id,
            'child_name': f"{child.first_name} {child.middle_name} {child.last_name}",
            'immunizations': record.immunizations,
        }
        immunizations.append(immunization_info)

    return render(request, 'all_immunizations.html', {'immunizations': immunizations})

def all_medical_conditions(request):
    health_records = HealthRecord.objects.order_by('-id')
    medical_conditions = []
    for record in health_records:
        child = record.child
        condition_info = {
            'child_id': child.id,
            'child_name': f"{child.first_name} {child.middle_name} {child.last_name}",
            'medical_conditions': record.medical_conditions,
        }
        medical_conditions.append(condition_info)

    return render(request, 'all_medical_conditions.html', {'medical_conditions': medical_conditions})

def all_emergency_contacts(request):
    all_emergency_contacts = EmergencyContact.objects.order_by('-id')
    return render(request, 'all_emergency_contacts.html', {'all_emergency_contacts': all_emergency_contacts})

def all_allergies(request):
    all_allergies = Allergy.objects.order_by('-id')
    return render(request, 'all_allergies.html', {'all_allergies': all_allergies})

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
    parents = Parent.objects.all().order_by('-id')[:5]
    relationships = ParentChildRelationship.objects.all().order_by('-id')[:5]
    return render(request, 'parent_list.html', {'parents': parents, 
                                                'relationships': relationships})
def all_parents(request):
    all_parents = Parent.objects.order_by('-id')
    return render(request, 'all_parents.html', {'all_parents': all_parents})

def all_child_parents_assignments(request):
    all_child_parents_assignments = ParentChildRelationship.objects.order_by('-id')
    return render(request, 'all_child_parents_assignments.html', {'all_child_parents_assignments': all_child_parents_assignments})

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

# def staff_list(request):
#     staffs = Staff.objects.all()
#     staff_child_assignments = StaffChildAssignment.objects.all()
#     staff_activity_assignments = StaffActivityAssignment.objects.all()
#     return render(request, 'staff_list.html', {
#         'staffs': staffs, 
#         'staff_child_assignments': staff_child_assignments,
#         'staff_activity_assignments': staff_activity_assignments
#     })

def staff_list(request):
    staffs = Staff.objects.order_by('-id')[:5]
    staff_child_assignments = StaffChildAssignment.objects.order_by('-id')[:5]
    staff_activity_assignments = StaffActivityAssignment.objects.order_by('-id')[:5]
    return render(request, 'staff_list.html', {
        'staffs': staffs, 
        'staff_child_assignments': staff_child_assignments,
        'staff_activity_assignments': staff_activity_assignments
    })

def all_staffs(request):
    all_staffs = Staff.objects.order_by('-id')
    return render(request, 'all_staffs.html', {'all_staffs': all_staffs})

def all_staff_child_assignments(request):
    all_staff_child_assignments = StaffChildAssignment.objects.order_by('-id')
    return render(request, 'all_staff_child_assignments.html', {'all_staff_child_assignments': all_staff_child_assignments})

def all_staff_activity_assignments(request):
    all_staff_activity_assignments = StaffActivityAssignment.objects.order_by('-id')
    return render(request, 'all_staff_activity_assignments.html', {'all_staff_activity_assignments': all_staff_activity_assignments})

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
    activities = Activity.objects.order_by('-id')[:5]  # Order by ID to get the most recently added entries
    child_activities_assignments = ChildActivityAssignment.objects.order_by('-id')[:5]  # Order by ID to get the most recently added entries
    return render(request, 'activity_list.html', {
        'activities': activities,
        'child_activities_assignments': child_activities_assignments
    })

def all_activities(request):
    all_activities = Activity.objects.order_by('-id')
    return render(request, 'all_activities.html', {'all_activities': all_activities})

def all_child_activities(request):
    all_child_activities_assignments = ChildActivityAssignment.objects.order_by('-id')
    return render(request, 'all_child_activities.html', {'all_child_activities_assignments': all_child_activities_assignments})


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
    attendances = Attendance.objects.order_by('-date')[:5]
    return render(request, 'attendance_list.html', {'attendances': attendances})

def all_attendances(request):
    all_attendances = Attendance.objects.order_by('-date')
    return render(request, 'all_attendances.html', {'all_attendances': all_attendances})

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
    return render(request, 'confirm_delete4.html', {'attendance': attendance})

def payment_list(request):
    payments = Payment.objects.order_by('-payment_date')[:5]
    child_expenses = ChildExpense.objects.order_by('-date')[:5]
    activity_expenses = ActivityExpense.objects.order_by('-date')[:5]
    other_expenses = OtherExpenses.objects.order_by('-date')[:5]
    return render(request, 'payment_list.html', {
        'payments': payments,
        'child_expenses': child_expenses,
        'activity_expenses': activity_expenses,
        'other_expenses': other_expenses
    })

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

def add_child_expense(request):
    if request.method == 'POST':
        form = ChildExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = ChildExpenseForm()
    return render(request, 'add_child_expense.html', {'form': form})

def edit_child_expense(request, pk):
    expense = get_object_or_404(ChildExpense, pk=pk)
    if request.method == 'POST':
        form = ChildExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = ChildExpenseForm(instance=expense)
    return render(request, 'edit__child_expense.html', {'form': form})

def delete_child_expense(request, pk):
    expense = get_object_or_404(ChildExpense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('payment_list')
    return render(request, 'confirm_delete6.html', {'object': expense})

def add_activity_expense(request):
    if request.method == 'POST':
        form = ActivityExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = ActivityExpenseForm()
    return render(request, 'add_activity_expense.html', {'form': form})

def edit_activity_expense(request, pk):
    expense = get_object_or_404(ActivityExpense, pk=pk)
    if request.method == 'POST':
        form = ActivityExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = ActivityExpenseForm(instance=expense)
    return render(request, 'edit__activity_expense.html', {'form': form})

def delete_activity_expense(request, pk):
    expense = get_object_or_404(ActivityExpense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('payment_list')
    return render(request, 'confirm_delete8.html', {'object': expense})

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

def search_child(request):
    child_id = request.GET.get('childID')
    first_name = request.GET.get('first_name')
    middle_name = request.GET.get('middle_name')
    last_name = request.GET.get('last_name')
    context = {}

    if child_id and first_name and last_name:
        try:
            child = Child.objects.get(
                id=child_id,
                first_name__iexact=first_name,
                middle_name__iexact=middle_name,
                last_name__iexact=last_name
            )
            child.age = calculate_age(child.date_of_birth)
            context["child"] = child

            try:
                health_record = HealthRecord.objects.get(child=child)
                context['health_record'] = health_record
            except HealthRecord.DoesNotExist:
                context['health_record'] = None

            try:
                emergency_contacts = EmergencyContact.objects.filter(child=child)
                context['emergency_contacts'] = emergency_contacts
            except EmergencyContact.DoesNotExist:
                context['emergency_contacts'] = None

            try:
                allergies = Allergy.objects.filter(child=child)
                context['allergies'] = allergies
            except Allergy.DoesNotExist:
                context['allergies'] = None

            try:
                relationships = ParentChildRelationship.objects.filter(child=child)
                parents = []
                for relationship in relationships:
                    parents.append(relationship.parent)
                context['parents'] = parents
            except ParentChildRelationship.DoesNotExist:
                context['parents'] = None

            return render(request, 'child_detail.html', context)

        except Child.DoesNotExist:
            context['invalid_child_id'] = True

    children = Child.objects.all()
    for child in children:
        child.age = calculate_age(child.date_of_birth)
        
    context['children'] = children
    context['health_records'] = HealthRecord.objects.all()
    context['emergency_contacts'] = EmergencyContact.objects.all()
    context['allergies'] = Allergy.objects.all()
    context['parents'] = ParentChildRelationship.objects.all()
    return render(request, 'child_enrollment.html', context)

    
def search_activity(request):
    child_id = request.GET.get('childID')
    first_name = request.GET.get('first_name')
    middle_name = request.GET.get('middle_name')
    last_name = request.GET.get('last_name')
    date = request.GET.get('date')
    context = {}

    if child_id and first_name and last_name and date:
        try:
            child = Child.objects.get(
                id=child_id,
                first_name__iexact=first_name,
                middle_name__iexact=middle_name,
                last_name__iexact=last_name
            )
            context['child'] = child
            context['date'] = date

            try:
                activity_assignments = ChildActivityAssignment.objects.filter(child=child, date=date)
                activities = [assignment.activity for assignment in activity_assignments]
                context['activities'] = activities
            except ChildActivityAssignment.DoesNotExist:
                context['activities'] = None

            try:
                staff_assignments = StaffChildAssignment.objects.filter(child=child, date=date)
                staff = [assignment.staff for assignment in staff_assignments]
                context['staff'] = staff
            except StaffChildAssignment.DoesNotExist:
                context['staff'] = None

            return render(request, 'child_activity_result.html', context)

        except Child.DoesNotExist:
            context['invalid_child_id_date'] = True

    context['children'] = Child.objects.all()
    context['health_records'] = HealthRecord.objects.all()
    context['emergency_contacts'] = EmergencyContact.objects.all()
    context['allergies'] = Allergy.objects.all()
    return render(request, 'child_enrollment.html', context)

def search_vaccine(request):
    vaccine = request.GET.get('vaccine')
    context = {}

    if vaccine:
        health_records = HealthRecord.objects.filter(immunizations__iexact=vaccine)
        children = [record.child for record in health_records]
        context['children'] = children
        if not vaccine:
            context['no_children'] = True

    return render(request, 'search_vaccine_results.html', context)

def search_condition(request):
    condition = request.GET.get('condition')
    context = {}

    if condition:
        health_records = HealthRecord.objects.filter(medical_conditions__iexact=condition)
        children = [record.child for record in health_records]
        context['children'] = children
        if not condition:
            context['no_children'] = True

    return render(request, 'search_condition_results.html', context)

def search_allergy(request):
    allergy = request.GET.get('allergy')
    context = {}

    if allergy:
        allergies = Allergy.objects.filter(allergy_name__iexact=allergy)
        children = [allergy.child for allergy in allergies]
        context['children'] = children
        if not allergies:
            context['no_children'] = True

    return render(request, 'search_allergy_results.html', context)

def search_emergency_id(request):
    emergency_id = request.GET.get('emergency_id')
    first_name = request.GET.get('first_name')
    middle_name = request.GET.get('middle_name')
    last_name = request.GET.get('last_name')
    context = {}

    if emergency_id and first_name and middle_name and last_name:
        emergency_contacts = EmergencyContact.objects.filter(
            id=emergency_id,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name
        )
        children = [contact.child for contact in emergency_contacts]
        context['children'] = children
        if not emergency_contacts:
            context['no_children'] = True
    else:
        context['error'] = "Please provide all required fields."

    return render(request, 'search_emergency_id_results.html', context)


def search_parent(request):
    parent_id = request.GET.get('parentID')
    first_name = request.GET.get('first_name')
    middle_name = request.GET.get('middle_name')
    last_name = request.GET.get('last_name')
    context = {}

    if parent_id and first_name and last_name:
        try:
            parent = Parent.objects.get(
                id=parent_id,
                first_name__iexact=first_name,
                middle_name__iexact=middle_name,
                last_name__iexact=last_name
            )
            relationships = ParentChildRelationship.objects.filter(parent=parent)
            children = [relationship.child for relationship in relationships]
            context['children'] = children
            if not children:
                context['no_children'] = True
        except Parent.DoesNotExist:
            context['no_children'] = True

    return render(request, 'search_parent_results.html', context)


def search_payments(request):
    parent_id = request.GET.get('parentID')
    first_name = request.GET.get('first_name')
    middle_name = request.GET.get('middle_name')
    last_name = request.GET.get('last_name')
    context = {}

    if parent_id and first_name and last_name:
        try:
            parent = Parent.objects.get(
                id=parent_id,
                first_name__iexact=first_name,
                middle_name__iexact=middle_name,
                last_name__iexact=last_name
            )
            payments = Payment.objects.filter(parent=parent)
            total_amount = payments.aggregate(Sum('amount_paid'))['amount_paid__sum'] or 0
            context['payments'] = payments
            context['total_amount'] = total_amount
            if not payments:
                context['no_payments'] = True
        except Parent.DoesNotExist:
            context['invalid_parent_id_payments'] = True

    return render(request, 'search_payments_results.html', context)

def search_activity_details(request):
    activity_id = request.GET.get('activityID')
    activity_name = request.GET.get('activityName')
    date = request.GET.get('date')
    context = {}

    activity = None
    invalid_activity_id = False
    no_matching_activity_name = False

    if activity_id:
        try:
            activity = Activity.objects.get(id=activity_id)
        except Activity.DoesNotExist:
            invalid_activity_id = True

    if activity_name:
        try:
            activity_name_obj = Activity.objects.get(activity_name__iexact=activity_name)
            if activity and activity != activity_name_obj:
                no_matching_activity_name = True
            else:
                activity = activity_name_obj
        except Activity.DoesNotExist:
            no_matching_activity_name = True

    if not invalid_activity_id and not no_matching_activity_name and activity and date:
        context['activity'] = activity
        context['date'] = date

        supervising_staff = StaffActivityAssignment.objects.filter(activity=activity, date=date).select_related('staff')
        context['supervising_staff'] = [assignment.staff for assignment in supervising_staff] if supervising_staff else None

        attending_children = ChildActivityAssignment.objects.filter(activity=activity, date=date).select_related('child')
        context['attending_children'] = [assignment.child for assignment in attending_children] if attending_children else None

        return render(request, 'activity_details.html', context)

    activities = Activity.objects.all()
    child_activity_assignments = ChildActivityAssignment.objects.all()
    context = {
        'activities': activities,
        'child_activities_assignments': child_activity_assignments,
        'invalid_activity_id': invalid_activity_id,
        'no_matching_activity_name': no_matching_activity_name,
    }

    return render(request, 'activity_list.html', context)

def search_activity_by_duration(request):
    date_str = request.GET.get('date')
    duration = request.GET.get('duration')
    context = {}

    if date_str and duration:
        # Parse the date input
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            context['invalid_date'] = True
            activities = Activity.objects.all()
            context['activities'] = activities
            return render(request, 'activity_list.html', context)

        # Define the duration filter using datetime.timedelta
        if duration == "less_than_10":
            duration_filter = {'duration__lt': timedelta(minutes=10)}
        elif duration == "10_to_30":
            duration_filter = {
                'duration__gte': timedelta(minutes=10),
                'duration__lte': timedelta(minutes=30)
            }
        elif duration == "more_than_30":
            duration_filter = {'duration__gt': timedelta(minutes=30)}
        else:
            duration_filter = {}

        # Apply the duration filter if valid
        activities = Activity.objects.filter(**duration_filter)

        # Filter activities by date using the related models
        activities = activities.filter(
            Q(staffactivityassignment__date=date) | Q(childactivityassignment__date=date)
        ).distinct()

        # Prepare the context with additional information
        activities_info = []
        for activity in activities:
            supervising_staff = StaffActivityAssignment.objects.filter(activity=activity, date=date).select_related('staff')
            attending_children = ChildActivityAssignment.objects.filter(activity=activity, date=date).select_related('child')
            activities_info.append({
                'activity': activity,
                'supervising_staff': supervising_staff,
                'attending_children': attending_children
            })

        context['activities_info'] = activities_info
        context['date'] = date
        context['duration'] = duration

        return render(request, 'activity_duration_details.html', context)

    context['invalid_search'] = True
    activities = Activity.objects.all()
    context['activities'] = activities
    return render(request, 'activity_list.html', context)


def search_staff(request):
    staff_id = request.GET.get('staffID')
    first_name = request.GET.get('first_name')
    middle_name = request.GET.get('middle_name')
    last_name = request.GET.get('last_name')
    date = request.GET.get('date')
    context = {}

    if staff_id and first_name and last_name and date:
        try:
            staff = Staff.objects.get(
                id=staff_id,
                first_name__iexact=first_name,
                middle_name__iexact=middle_name,
                last_name__iexact=last_name
            )
            context['staff'] = staff
            context['date'] = date

            try:
                staff_activity_assignments = StaffActivityAssignment.objects.filter(staff=staff, date=date)
                activities = [assignment.activity for assignment in staff_activity_assignments]
                context['activities'] = activities
            except StaffActivityAssignment.DoesNotExist:
                context['activities'] = None

            try:
                staff_child_assignments = StaffChildAssignment.objects.filter(staff=staff, date=date)
                children = [assignment.child for assignment in staff_child_assignments]
                context['children'] = children
            except StaffChildAssignment.DoesNotExist:
                context['children'] = None

            return render(request, 'staff_activity_result.html', context)

        except Staff.DoesNotExist:
            context['invalid_staff_id_date'] = True

    else:
        context['invalid_staff_id_date'] = True

    staff_list = Staff.objects.all()
    staff_child_assignments = StaffChildAssignment.objects.all()
    staff_activity_assignments = StaffActivityAssignment.objects.all()
    context.update({
        'staffs': staff_list,
        'staff_child_assignments': staff_child_assignments,
        'staff_activity_assignments': staff_activity_assignments
    })

    return render(request, 'staff_list.html', context)


def search_attendance_by_date(request):
    date = request.GET.get('date')
    context = {}

    if date:
        attendance_records = Attendance.objects.filter(date=date, is_present = True)
        context['attendance_records'] = attendance_records
        context['date'] = date
        return render(request, 'attendance_result_list.html', context)

    context['invalid_search'] = True
    attendance_records = Attendance.objects.all()
    context['attendance_records'] = attendance_records
    return render(request, 'attendance_result_list.html', context)


def search_absent_by_date(request):
    date = request.GET.get('date')
    context = {}

    if date:
        absent_records = Attendance.objects.filter(date=date, is_present=False)
        context['absent_records'] = absent_records
        context['date'] = date
        return render(request, 'absent_result_list.html', context)

    context['invalid_search'] = True
    absent_records = Attendance.objects.filter(is_present=False)
    context['absent_records'] = absent_records
    return render(request, 'absent_result_list.html', context)

def attendance_last_7_days(request):
    today = timezone.now().date()
    last_week = today - timedelta(days=7)
    attendance_records = Attendance.objects.filter(date__range=[last_week, today], is_present = True)
    context = {
        'attendance_records': attendance_records,
        'last_week': last_week,
        'today': today
    }
    return render(request, 'attendance_last_7_days.html', context)

def absent_last_7_days(request):
    today = timezone.now().date()
    last_week = today - timedelta(days=7)
    absent_records = Attendance.objects.filter(date__range=[last_week, today], is_present=False)
    context = {
        'absent_records': absent_records,
        'last_week': last_week,
        'today': today
    }
    return render(request, 'absent_last_7_days.html', context)

def attendance_last_30_days(request):
    today = timezone.now().date()
    last_month = today - timedelta(days=30)
    attendance_records = Attendance.objects.filter(date__range=[last_month, today])
    context = {
        'attendance_records': attendance_records,
        'last_month': last_month,
        'today': today
    }
    return render(request, 'attendance_last_30_days.html', context)

def absent_last_30_days(request):
    today = timezone.now().date()
    last_month = today - timedelta(days=30)
    absent_records = Attendance.objects.filter(date__range=[last_month, today], is_present=False)
    context = {
        'absent_records': absent_records,
        'last_month': last_month,
        'today': today
    }
    return render(request, 'absent_last_30_days.html', context)

def payments_last_7_days(request):
    today = timezone.now().date()
    seven_days_ago = today - timedelta(days=7)
    payments = Payment.objects.filter(payment_date__range=[seven_days_ago, today])
    total_amount = sum(payment.amount_paid for payment in payments)

    context = {
        'total_amount': total_amount,
        'payments': payments,
    }

    return render(request, 'payments_last_7_days.html', context)

def payments_last_30_days(request):
    today = timezone.now().date()
    thirty_days_ago = today - timedelta(days=30)
    payments = Payment.objects.filter(payment_date__range=[thirty_days_ago, today])
    total_amount = sum(payment.amount_paid for payment in payments)

    context = {
        'total_amount': total_amount,
        'payments': payments,
    }

    return render(request, 'payments_last_30_days.html', context)

def calculate_total_expenses(expenses):
    return sum(expense.amount for expense in expenses)

def child_expenses(request):
    context = {
        'child_expenses': ChildExpense.objects.all()
    }
    return render(request, 'child_expenses.html', context)

def child_expenses_last_7_days(request):
    today = timezone.now().date()
    seven_days_ago = today - timedelta(days=7)
    expenses = ChildExpense.objects.filter(date__range=[seven_days_ago, today])
    total_amount = calculate_total_expenses(expenses)

    context = {
        'child_expenses': expenses,
        'total_amount': total_amount
    }
    return render(request, 'child_expenses_last_7_days.html', context)

def child_expenses_last_30_days(request):
    today = timezone.now().date()
    thirty_days_ago = today - timedelta(days=30)
    expenses = ChildExpense.objects.filter(date__range=[thirty_days_ago, today])
    total_amount = calculate_total_expenses(expenses)

    context = {
        'child_expenses': expenses,
        'total_amount': total_amount
    }
    return render(request, 'child_expenses_last_30_days.html', context)

def all_child_expenses(request):
    expenses = ChildExpense.objects.all()
    total_amount = calculate_total_expenses(expenses)

    context = {
        'child_expenses': expenses,
        'total_amount': total_amount
    }
    return render(request, 'child_expenses_all.html', context)

def calculate_total_expenses(expenses):
    return sum(expense.amount for expense in expenses)

def activity_expenses(request):
    context = {
        'activity_expenses': ActivityExpense.objects.all()
    }
    return render(request, 'activity_expenses.html', context)

def activity_expenses_last_7_days(request):
    today = timezone.now().date()
    seven_days_ago = today - timedelta(days=7)
    expenses = ActivityExpense.objects.filter(date__range=[seven_days_ago, today])
    total_amount = calculate_total_expenses(expenses)

    context = {
        'activity_expenses': expenses,
        'total_amount': total_amount
    }
    return render(request, 'activity_expenses_last_7_days.html', context)

def activity_expenses_last_30_days(request):
    today = timezone.now().date()
    thirty_days_ago = today - timedelta(days=30)
    expenses = ActivityExpense.objects.filter(date__range=[thirty_days_ago, today])
    total_amount = calculate_total_expenses(expenses)

    context = {
        'activity_expenses': expenses,
        'total_amount': total_amount
    }
    return render(request, 'activity_expenses_last_30_days.html', context)

def all_activity_expenses(request):
    expenses = ActivityExpense.objects.all()
    total_amount = calculate_total_expenses(expenses)

    context = {
        'activity_expenses': expenses,
        'total_amount': total_amount
    }
    return render(request, 'activity_expenses_all.html', context)

def calculate_total_expenses(expenses):
    return sum(expense.amount for expense in expenses)

def other_expenses(request):
    context = {
        'other_expenses': OtherExpenses.objects.all()
    }
    return render(request, 'other_expenses.html', context)

def other_expenses_last_7_days(request):
    today = timezone.now().date()
    seven_days_ago = today - timedelta(days=7)
    expenses = OtherExpenses.objects.filter(date__range=[seven_days_ago, today])
    total_amount = calculate_total_expenses(expenses)

    context = {
        'other_expenses': expenses,
        'total_amount': total_amount
    }
    return render(request, 'other_expenses_last_7_days.html', context)

def other_expenses_last_30_days(request):
    today = timezone.now().date()
    thirty_days_ago = today - timedelta(days=30)
    expenses = OtherExpenses.objects.filter(date__range=[thirty_days_ago, today])
    total_amount = calculate_total_expenses(expenses)

    context = {
        'other_expenses': expenses,
        'total_amount': total_amount
    }
    return render(request, 'other_expenses_last_30_days.html', context)

def all_other_expenses(request):
    expenses = OtherExpenses.objects.all()
    total_amount = calculate_total_expenses(expenses)

    context = {
        'other_expenses': expenses,
        'total_amount': total_amount
    }
    return render(request, 'other_expenses_all.html', context)

def all_payments(request):
    all_payments = Payment.objects.order_by('-payment_date')
    return render(request, 'all_payments.html', {'all_payments': all_payments})
