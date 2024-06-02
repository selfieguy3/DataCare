from django.shortcuts import render
from django.http import HttpResponse
from myapp.utils import add_person, remove_person
from myapp.models import Person


def add_person_view(request):
    if request.method == 'GET':
        return render(request, 'add_person.html')
    elif request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        age = int(request.POST.get('age'))
        person_type = request.POST.get('person_type')

        person = add_person(first_name, middle_name, last_name, age, person_type)
        return HttpResponse(f"Added {person.P_FName} {person.P_LName}")

def remove_person_view(request, person_id):
    # Example of removing a person
    success = remove_person(person_id)
    if success:
        return HttpResponse("Person removed successfully")
    else:
        return HttpResponse("Person not found")
