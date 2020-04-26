import datetime

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from .models import CustomerUser, Courses, Subjects, Staffs, Students
from .forms import AddStudentForm, EditStudentForm


def StudentAdmin(request):
    return render(request, 'student_admin.html')

