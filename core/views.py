from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Doctor, Patient

def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')

    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/login/')


def home(request):
    return render(request, 'core/home.html')


def doctors(request):
    doctor_list = Doctor.objects.all()
    return render(request, 'core/doctors.html', {'doctor_list': doctor_list})


def patients(request):
    patient_list = Patient.objects.all()
    return render(request, 'core/patients.html', {'patient_list': patient_list})