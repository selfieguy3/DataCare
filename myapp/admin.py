from django.contrib import admin
from .models import Staff, Activity, StaffChildAssignment, StaffActivityAssignment

admin.site.register(Staff)
admin.site.register(Activity)
admin.site.register(StaffChildAssignment)
admin.site.register(StaffActivityAssignment)
