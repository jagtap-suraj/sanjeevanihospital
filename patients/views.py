from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import Patient

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def add_patient(request):
    form = PatientForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    return render(request, 'patient_form.html', {'form': form})

def edit_patient(request, pk):
    patient = Patient.objects.get(pk=pk)
    form = PatientForm(request.POST or None, instance=patient)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    return render(request, 'patient_form.html', {'form': form})

def delete_patient(request, pk):
    patient = Patient.objects.get(pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patient_confirm_delete.html', {'patient': patient})
