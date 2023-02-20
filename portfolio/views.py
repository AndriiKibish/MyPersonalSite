from django.shortcuts import render
from .models import Project, Certificate


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def certificates(request):
    certificates = Certificate.objects.all()
    return render(request, 'portfolio/certificates.html', {'certificates': certificates})
