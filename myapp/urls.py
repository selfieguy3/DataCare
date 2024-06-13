from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('child-enrollment/', views.child_enrollment, name='child_enrollment'),
    path('add-child/', views.add_child, name='add_child'),
    path('edit-child/<int:pk>/', views.edit_child, name='edit_child'),
    path('delete-child/<int:pk>/', views.delete_child, name='delete_child'),
    path('add-health-record/', views.add_health_record, name='add_health_record'),
    path('edit-health-record/<int:pk>/', views.edit_health_record, name='edit_health_record'),
    path('delete-health-record/<int:pk>/', views.delete_health_record, name='delete_health_record'),
    path('add-emergency-contact/', views.add_emergency_contact, name='add_emergency_contact'),
    path('edit-emergency-contact/<int:pk>/', views.edit_emergency_contact, name='edit_emergency_contact'),
    path('delete-emergency-contact/<int:pk>/', views.delete_emergency_contact, name='delete_emergency_contact'),
    path('add-allergy/', views.add_allergy, name='add_allergy'),
    path('edit-allergy/<int:pk>/', views.edit_allergy, name='edit_allergy'),
    path('delete-allergy/<int:pk>/', views.delete_allergy, name='delete_allergy'),
    path('parents/', views.parent_list, name='parent_list'),
    path('add-parents/', views.add_parent, name='add_parent'),
    path('edit/<int:parent_id>/', views.edit_parent, name='edit_parent'),
    path('delete/<int:parent_id>/', views.delete_parent, name='delete_parent'),
    path('assign/', views.assign_child, name='assign_child'),
    path('edit_relationship/<int:relationship_id>/', views.edit_relationship, name='edit_relationship'),
    path('delete_relationship/<int:relationship_id>/', views.delete_relationship, name='delete_relationship'),
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/add/', views.staff_add, name='staff_add'),
    path('staff/edit/<int:pk>/', views.staff_edit, name='staff_edit'),
    path('staff/delete/<int:pk>/', views.staff_delete, name='staff_delete'),
    path('assign_staff_child/', views.assign_staff_child, name='assign_staff_child'),
    path('assign_staff_activity/', views.assign_staff_activity, name='assign_staff_activity'),
    path('delete_staff_child_assignment/<int:assignment_id>/', views.delete_staff_child_assignment, name='delete_staff_child_assignment'),
    path('delete_staff_activity_assignment/<int:assignment_id>/', views.delete_staff_activity_assignment, name='delete_staff_activity_assignment'),
    path('edit_staff_child_assignment/<int:assignment_id>/', views.edit_staff_child_assignment, name='edit_staff_child_assignment'),
    path('edit_staff_activity_assignment/<int:assignment_id>/', views.edit_staff_activity_assignment, name='edit_staff_activity_assignment'),
    path('activities/', views.activity_list, name='activity_list'),
    path('activities/add/', views.activity_add, name='activity_add'),
    path('activities/edit/<int:pk>/', views.activity_edit, name='activity_edit'),
    path('activities/delete/<int:pk>/', views.activity_delete, name='activity_delete'),
    path('activities/assign/', views.assign_activity_child, name='assign_activity_child'),
    path('activities/assign/edit/<int:assignment_id>/', views.edit_activity_assignment, name='edit_activity_assignment'),
    path('activities/assign/delete/<int:assignment_id>/', views.delete_activity_assignment, name='delete_activity_assignment'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.add_attendance, name='add_attendance'),
    path('attendance/edit/<int:pk>/', views.edit_attendance, name='edit_attendance'),
    path('attendance/delete/<int:pk>/', views.delete_attendance, name='delete_attendance'),
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/add/', views.add_payment, name='add_payment'),
    path('payments/edit/<int:pk>/', views.edit_payment, name='edit_payment'),
    path('payments/delete/<int:pk>/', views.delete_payment, name='delete_payment'),
    path('child_expenses/add/', views.add_child_expense, name='add_child_expense'),
    path('child_expenses/edit/<int:pk>/', views.edit_child_expense, name='edit_child_expense'),
    path('child_expenses/delete/<int:pk>/', views.delete_child_expense, name='delete_child_expense'),
    path('activity_expenses/add/', views.add_activity_expense, name='add_activity_expense'),
    path('activity_expenses/edit/<int:pk>/', views.edit_activity_expense, name='edit_activity_expense'),
    path('activity_expenses/delete/<int:pk>/', views.delete_activity_expense, name='delete_activity_expense'),
    path('other_expenses/add/', views.add_other_expense, name='add_other_expense'),
    path('other_expenses/edit/<int:pk>/', views.edit_other_expense, name='edit_other_expense'),
    path('other_expenses/delete/<int:pk>/', views.delete_other_expense, name='delete_other_expense'),
    path('search_child/', views.search_child, name='search_child'),
    path('search_activity/', views.search_activity, name='search_activity'),
    path('search_vaccine/', views.search_vaccine, name='search_vaccine'),
    path('search_condition/', views.search_condition, name='search_condition'),
    path('search_allergy/', views.search_allergy, name='search_allergy'),
    path('search_emergency_id/', views.search_emergency_id, name='search_emergency_id'),
    path('search_parent/', views.search_parent, name='search_parent'),
    path('search_payments/', views.search_payments, name='search_payments'),
    path('search_staff/', views.search_staff, name='search_staff'),
    path('search_activity_details/', views.search_activity_details, name='search_activity_details'),
    path('search_activity_by_duration/', views.search_activity_by_duration, name='search_activity_by_duration'),
    path('is_attendance/', views.search_attendance_by_date, name='search_attendance_by_date'),
    path('is_absent/', views.search_absent_by_date, name='search_absent_by_date'),
    path('attendance_last_7_days/', views.attendance_last_7_days, name='attendance_last_7_days'),
    path('absent_last_7_days/', views.absent_last_7_days, name='absent_last_7_days'),
    path('attendance_last_30_days/', views.attendance_last_30_days, name='attendance_last_30_days'),
    path('absent_last_30_days/', views.absent_last_30_days, name='absent_last_30_days'),
    path('payments/last-7-days/', views.payments_last_7_days, name='payments_last_7_days'),
    path('payments/last-30-days/', views.payments_last_30_days, name='payments_last_30_days'),
    path('child_expenses/last_7_days/', views.child_expenses_last_7_days, name='child_expenses_last_7_days'),
    path('child_expenses/last_30_days/', views.child_expenses_last_30_days, name='child_expenses_last_30_days'),
    path('child_expenses/all/', views.all_child_expenses, name='all_child_expenses'),
    path('activity_expenses/last_7_days/', views.activity_expenses_last_7_days, name='activity_expenses_last_7_days'),
    path('activity_expenses/last_30_days/', views.activity_expenses_last_30_days, name='activity_expenses_last_30_days'),
    path('activity_expenses/all/', views.all_activity_expenses, name='all_activity_expenses'),
    path('other_expenses/last_7_days/', views.other_expenses_last_7_days, name='other_expenses_last_7_days'),
    path('other_expenses/last_30_days/', views.other_expenses_last_30_days, name='other_expenses_last_30_days'),
    path('other_expenses/all/', views.all_other_expenses, name='all_other_expenses'),
    path('payments/all/', views.all_payments, name='all_payments'),
    path('attendance/all/', views.all_attendances, name='all_attendances'),
    path('activity/all/', views.all_activities, name='all_activities'),
    path('activity/child_all/', views.all_child_activities, name='all_child_activities'),
    path('staff/all/', views.all_staffs, name='all_staffs'),
    path('staff/child_all/', views.all_staff_child_assignments, name='all_staff_child_assignments'),
    path('staff/activity_all/', views.all_staff_activity_assignments, name='all_staff_activity_assignments'),
    path('parent/all/', views.all_parents, name='all_parents'),
    path('parent/child_all/', views.all_child_parents_assignments, name='all_child_parents_assignments'),
    path('all_children/', views.all_children, name='all_children'),
    path('all_immunizations/', views.all_immunizations, name='all_immunizations'),
    path('all_medical_conditions/', views.all_medical_conditions, name='all_medical_conditions'),
    path('all_emergency_contacts/', views.all_emergency_contacts, name='all_emergency_contacts'),
    path('all_allergies/', views.all_allergies, name='all_allergies'),
]
