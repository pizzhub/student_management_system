"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from student_management_app import views, hodViews
from student_management_system import settings

urlpatterns = [
    path('demo', views.showDemoPage),
    path('login', views.showLoginPage),
    path('doLogin', views.doLogin),
    path('get_user_detail', views.GetUserDetail),
    path('logout_user', views.LogoutUser),
    path('dashboard', hodViews.Dashboard),

    path('add_staff', hodViews.AddStaff),
    path('add_staff_save', hodViews.AddStaffSave),

    path('add_student', hodViews.AddStudent),
    path('add_student_save', hodViews.AddStudentSave),

    path('add_course', hodViews.AddCourse),
    path('add_course_save', hodViews.AddCourseSave),

    path('add_subject', hodViews.AddSubject),
    path('add_subject_save', hodViews.AddSubjectSave),

    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
