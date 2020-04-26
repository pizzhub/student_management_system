import datetime

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from .models import CustomerUser, Courses, Subjects, Staffs, Students
from .forms import AddStudentForm, EditStudentForm


def Dashboard(request):
    return render(request, 'admin.html')


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
            return HttpResponseRedirect(reverse('add_staff'))
        except:
            messages.error(request, "An error occurred!")
            return HttpResponseRedirect(reverse('add_staff'))


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
            return HttpResponseRedirect(reverse('add_course'))
        except:
            messages.error(request, "An error occurred!")
            return HttpResponseRedirect(reverse('add_course'))


def AddStudent(request):
    form = AddStudentForm()
    context = {}
    courses = Courses.objects.all()

    context['courses'] = courses
    context['form'] = form

    return render(request, 'students/add.html', context)


def AddStudentSave(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            address = form.cleaned_data["address"]
            course_id = form.cleaned_data["course"]
            gender = form.cleaned_data["gender"]
            session_start = form.cleaned_data["session_start"]
            session_end = form.cleaned_data["session_end"]

            try:
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            except MultiValueDictKeyError:
                profile_pic_url = None

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
                user.students.session_start_year = session_start
                user.students.session_end_year = session_end
                if profile_pic_url is not None:
                    user.students.profile_pic = profile_pic_url
                user.save()
                messages.success(request, "Added staff successfully!")
                return HttpResponseRedirect(reverse('add_student'))
            except:
                messages.error(request, "An error occurred!")
                return HttpResponseRedirect(reverse('add_student'))
        else:
            form = AddStudentForm(request.POST)
            return render(request, 'students/add.html', {"form": form})


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
        course_id = request.POST.get("course")
        course = Courses.objects.get(id=course_id)
        staff_id = request.POST.get("staff")
        staff = CustomerUser.objects.get(id=staff_id)
        try:
            subject = Subjects(
                subject_name=subject_name,
                course_id=course,
                staff_id=staff
            )
            subject.save()
            messages.success(request, "Added Subject Successfully!")
            return HttpResponseRedirect(reverse('add_subject'))
        except:
            messages.error(request, "An error occurred!")
            return HttpResponseRedirect(reverse('add_subject'))


def ListStaff(request):
    context = {}
    staffs = Staffs.objects.all()
    context['staffs'] = staffs

    return render(request, 'staffs/list.html', context)


def ListStudent(request):
    context = {}
    students = Students.objects.all()
    context['students'] = students

    return render(request, 'students/list.html', context)


def ListCourse(request):
    context = {}
    courses = Courses.objects.all()
    context['courses'] = courses

    return render(request, 'courses/list.html', context)


def ListSubject(request):
    context = {}
    subjects = Subjects.objects.all()
    context['subjects'] = subjects

    return render(request, 'subjects/list.html', context)


def EditStaff(request, staff_id):
    context = {}

    staff = Staffs.objects.get(admin=staff_id)
    context['staff'] = staff
    context['id'] = staff_id

    return render(request, 'staffs/edit.html', context)


def EditStaffSave(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        staff_id = request.POST.get("staff_id")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        address = request.POST.get("address")
        try:
            user = CustomerUser.objects.get(id=staff_id)
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.save()

            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()

            messages.success(request, "Successfully Edit Staff")
            return HttpResponseRedirect(reverse("edit_staff", kwargs={"staff_id": staff_id}))
        except:
            messages.error(request, "An error occurred")
            return HttpResponseRedirect(reverse("edit_staff", kwargs={"staff_id": staff_id}))


def EditStudent(request, student_id):
    request.session["student_id"] = student_id
    form = EditStudentForm()
    context = {}

    courses = Courses.objects.all()
    student = Students.objects.get(admin=student_id)

    form.fields['email'].initial = student.admin.email
    form.fields['first_name'].initial = student.admin.first_name
    form.fields['last_name'].initial = student.admin.last_name
    form.fields['username'].initial = student.admin.username
    form.fields['address'].initial = student.address
    form.fields['course'].initial = student.course_id.id
    form.fields['gender'].initial = student.gender
    form.fields['session_start'].initial = student.session_start_year
    form.fields['session_end'].initial = student.session_end_year

    context['student'] = student
    context['courses'] = courses
    context['id'] = student_id
    context['form'] = form

    return render(request, 'students/edit.html', context)


def EditStudentSave(request):
    context = {}

    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        student_id = request.session.get("student_id")
        if student_id is None:
            return HttpResponseRedirect(reverse("list_student"))

        form = EditStudentForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            address = form.cleaned_data["address"]
            course_id = form.cleaned_data["course"]
            gender = form.cleaned_data["gender"]
            session_start = form.cleaned_data["session_start"]
            session_end = form.cleaned_data["session_end"]

            if request.FILES.get('profile_pic', False):
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None

            try:
                user = CustomerUser.objects.get(id=student_id)
                user.email = email
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.save()

                student_model = Students.objects.get(admin=student_id)
                student_model.address = address
                student_model.session_start_year = session_start
                student_model.session_end_year = session_end
                student_model.gender = gender
                course = Courses.objects.get(id=course_id)
                student_model.course_id = course
                if profile_pic_url is not None:
                    student_model.profile_pic = profile_pic_url

                student_model.save()
                del request.session["student_id"]

                messages.success(request, "Successfully Edit Student")
                return HttpResponseRedirect(reverse("edit_student", kwargs={"student_id": student_id}))
            except:
                messages.error(request, "An error occurred")
                return HttpResponseRedirect(reverse("edit_student", kwargs={"student_id": student_id}))
        else:
            form = EditStudentForm(request.POST)

            context['form'] = form
            return render(request, 'students/edit.html', context)


def EditSubject(request, subject_id):
    context = {}

    courses = Courses.objects.all()
    staffs = CustomerUser.objects.filter(user_type=2)

    subject = Subjects.objects.get(id=subject_id)
    context['subject'] = subject
    context['courses'] = courses
    context['staffs'] = staffs
    context['id'] = subject_id

    return render(request, 'subjects/edit.html', context)


def EditSubjectSave(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course')
        staff_id = request.POST.get('staff')

        try:
            subject = Subjects.objects.get(id=subject_id)
            subject.subject_name = subject_name
            course = Courses.objects.get(id=course_id)
            subject.course_id = course
            staff = CustomerUser.objects.get(id=staff_id)
            subject.staff_id = staff

            subject.save()

            messages.success(request, "Successfully Edit Subject")
            return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id": subject_id}))
        except:
            messages.error(request, "An error occurred")
            return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id": subject_id}))


def EditCourse(request, course_id):
    context = {}

    course = Courses.objects.get(id=course_id)
    context['course'] = course
    context['id'] = course_id

    return render(request, 'courses/edit.html', context)


def EditCourseSave(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course_name')

        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name

            course.save()

            messages.success(request, "Successfully Edit Course")
            return HttpResponseRedirect(reverse("edit_course", kwargs={"course_id": course_id}))
        except:
            messages.error(request, "An error occurred")
            return HttpResponseRedirect(reverse("edit_course", kwargs={"course_id": course_id}))
