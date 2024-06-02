from myapp.models import Person

def add_person(first_name, middle_name, last_name, age, person_type):
    person = Person(
        P_FName=first_name,
        P_MName=middle_name,
        P_LName=last_name,
        Age=age,
        Person_Type=person_type
    )
    person.save()
    return person

def remove_person(person_id):
    try:
        person = Person.objects.get(P_ID=person_id)
        person.delete()
        return True
    except Person.DoesNotExist:
        return False
