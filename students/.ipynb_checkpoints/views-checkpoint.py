from django.shortcuts import render
from .forms import StudentForm


def student_form(request):
    return render(request, 'students/student_form.html')


def success(request):
    return render(request, 'students/success.html')