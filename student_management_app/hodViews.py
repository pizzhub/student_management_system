import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from student_management_app.models import CustomerUser, Courses, Subjects, Staffs


def Dashboard(request):
    return render(request, 'dashboard.html')


def AddStaff(request):
    return render(request, 'staffs/add.html')


def AddStaffSave(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomerUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
                user_type=2
            )
            user.staffs.address = address
            user.save()
            messages.success(request, "Added staff successfully!")
            return HttpResponseRedirect('/add_staff')
        except:
            messages.error(request, "An error occurred!")
            return HttpResponseRedirect('/add_staff')


def AddCourse(request):
    return render(request, 'courses/add.html')


def AddCourseSave(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        course_name = request.POST.get("course_name")
        try:
            course = Courses(
                course_name=course_name
            )
            course.save()
            messages.success(request, "Added Course successfully!")
            return HttpResponseRedirect('/add_course')
        except:
            messages.error(request, "An error occurred!")
            return HttpResponseRedirect('/add_course')


def AddStudent(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'students/add.html', context)


def AddStudentSave(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        course_id = request.POST.get("course")
        gender = request.POST.get("gender")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        try:
            user = CustomerUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
                user_type=3
            )
            user.students.address = address
            course_obj = Courses.objects.get(id=course_id)
            user.students.course_id = course_obj
            user.students.gender = gender

            # start_date = datetime.datetime.strptime(session_start, "%d-%m-%y").strftime("%Y-%m-%d")
            # end_date = datetime.datetime.strptime(session_end, "%d-%m-%y").strftime("%Y-%m-%d")

            user.students.session_start_year = session_start
            user.students.session_end_year = session_end
            user.students.profile_pic = ""
            user.save()
            messages.success(request, "Added staff successfully!")
            return HttpResponseRedirect('/add_student')
        except:
            messages.error(request, "An error occurred!")
            return HttpResponseRedirect('/add_student')


def AddSubject(request):
    courses = Courses.objects.all()
    staffs = CustomerUser.objects.filter(user_type=2)
    context = {
        "courses": courses,
        "staffs": staffs
    }
    return render(request, "subjects/add.html", context)


def AddSubjectSave(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        subject_name = request.POST.get("subject_name")
        try:
            subject = Subjects(
                subject_name=subject_name
            )
            subject.save()
            messages.success(request, "Added Subject Successfully!")
            return HttpResponseRedirect('/add_subject')
        except:
            messages.error(request, "An error occurred!")
            return HttpResponseRedirect('/add_subject')