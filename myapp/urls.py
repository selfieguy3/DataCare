from django.urls import path
from . import views

urlpatterns = [
    path('add-person/', views.add_person_view, name='add_person'),
    path('remove-person/<int:person_id>/', views.remove_person_view, name='remove_person'),
]
