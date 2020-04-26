from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student_management_app.EmailBackEnd import EmailBackEnd


def showDemoPage(request):
    return render(request, 'demo.html')


def showLoginPage(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = EmailBackEnd.authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse('dashboard'))
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staff_admin"))
            elif user.user_type == "3":
                return HttpResponseRedirect(reverse("student_admin"))
        else:
            messages.error(request, "Invalid Email Or Password, Please try again!")
            return HttpResponseRedirect("/login")


def GetUserDetail(request):
    if request.user.is_authenticated:
        return HttpResponse("User : " + request.user.email + " usertype : " + str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")


def LogoutUser(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect('/login')

