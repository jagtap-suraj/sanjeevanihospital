from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'address', 'dob', 'contact_number', 'blood_group', 'relative_name', 'relative_address', 'reason_for_admission']
