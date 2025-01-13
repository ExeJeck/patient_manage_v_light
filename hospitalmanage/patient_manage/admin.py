from django.contrib import admin

from .models import Patient, Doctor, Diagnosis, Appointment

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Diagnosis)
admin.site.register(Appointment)