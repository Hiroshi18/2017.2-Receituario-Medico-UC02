from django import forms
from user.models import Patient


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('name', 'date_of_birth', 'phone', 'email', 'sex',
                  'id_document')
