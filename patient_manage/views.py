from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .forms import PatientForm
from .models import Patient, Doctor, Appointment, Diagnosis

# Create your views here.
class HomePageView(generic.ListView):
    template_name = "patient_manage/home_page.html"
    context_object_name = "appointments"
    model = Appointment


class PatientsListView(generic.ListView):
    template_name = "patient_manage/patients_page.html"
    context_object_name = "patients"
    model = Patient
    

def about_page(request):
    return render(request, 'patient_manage/about_page.html')


def contacts_page(request):
    return render(request, 'patient_manage/contacts_page.html')


def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_manage:home_page')
    else:
        form = PatientForm()

    return render(request, 'patient_manage/patient_create.html', {'form': form})


def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_manage:patients_page')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'patient_manage/patient_update.html', {'form': form})


def record_delete(request):
    try:
        selected_model_name = request.POST["model"]
        selected_pk = request.POST["pk"]
    except KeyError:
        print("KeyError")
        return redirect('patient_manage:patients_page')
    else:
        if selected_model_name == "Patient":
            Patient.objects.get(pk=selected_pk).delete()
        elif selected_model_name == "Doctor":
            Doctor.objects.get(pk=selected_pk).delete()
        elif selected_model_name == "Diagnosis":
            Diagnosis.objects.get(pk=selected_pk).delete()
        elif selected_model_name == "Appointment":
            Appointment.objects.get(pk=selected_pk).delete()
        else:
            return redirect('patient_manage:patients_page')
        return redirect('patient_manage:patients_page')


def test_time(request):
    return HttpResponse(f'{timezone.localtime(timezone.now())}')