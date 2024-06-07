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
]

