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

]

