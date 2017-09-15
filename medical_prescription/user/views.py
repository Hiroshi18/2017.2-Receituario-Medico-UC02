from django.shortcuts import render, redirect, get_object_or_404
from user.models import Patient
from user.forms import PatientForm

def patient_view(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    template_name = ''
    context = {
        'patient': patient
    }
    return render(request, template_name, context)


def patient_register(request):
    template_name = 'templates/register.html'
    template_redirect = 'templates/register-sucess.html'

    if request.method == "POST":
        form = PatientForm(request.POST)

        if form.is_valid():
            patient = form.save(commit=False)
            patient.name = form.cleaned_data.get('name')
            patient.date_of_birth = form.cleaned_data.get('date_of_birth')
            patient.phone = form.cleaned_data.get('phone')
            patient.email = form.cleaned_data.get('email')
            patient.sex = form.cleaned_data.get('sex')
            patient.id_document = form.cleaned_data.get('id_document')
            patient.save()
            return redirect(template_redirect)
        else:
            # Nothing to do.
            pass
    else:
        form = PatientForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


def patient_edit(request, pk):
    template_name = ''
    template_redirect = ''
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():
            patient.name = form.cleaned_data.get('name')
            patient.date_of_birth = form.cleaned_data.get('date_of_birth')
            patient.phone = form.cleaned_data.get('phone')
            patient.email = form.cleaned_data
            patient.sex = form.cleaned_data.get('sex')
            patient.id_document = form.cleaned_data('id_document')
            patient.save()
            return redirect(template_redirect)
        else:
            # Nothing to do.
            pass
    else:
        form = PatientForm(instance=patient)
    context = {
        'form':
        form
    }
    return render(request, template_name, context)
