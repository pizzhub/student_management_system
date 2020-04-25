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

from student_management_app import views, HodViews
from student_management_system import settings

urlpatterns = [
    path('demo', views.showDemoPage),
    path('login', views.showLoginPage, name="login"),
    path('doLogin', views.doLogin, name="do_login"),
    path('get_user_detail', views.GetUserDetail, name="user_detail"),
    path('logout_user', views.LogoutUser, name="logout"),
    path('dashboard', HodViews.Dashboard, name="dashboard"),

    path('add_staff', HodViews.AddStaff, name="add_staff"),
    path('add_staff_save', HodViews.AddStaffSave, name="add_staff_save"),
    path('list_staff', HodViews.ListStaff, name="list_staff"),
    path('edit_staff/<str:staff_id>', HodViews.EditStaff, name="edit_staff"),
    path('edit_staff_save', HodViews.EditStaffSave, name="edit_staff_save"),

    path('add_student', HodViews.AddStudent, name="add_student"),
    path('add_student_save', HodViews.AddStudentSave, name="add_student_save"),
    path('list_student', HodViews.ListStudent, name="list_student"),
    path('edit_student/<str:student_id>', HodViews.EditStudent, name="edit_student"),
    path('edit_student_save', HodViews.EditStudentSave, name="edit_student_save"),

    path('add_course', HodViews.AddCourse, name="add_course"),
    path('add_course_save', HodViews.AddCourseSave, name="add_course_save"),
    path('list_course', HodViews.ListCourse, name="list_course"),
    path('edit_course/<str:course_id>', HodViews.EditCourse, name="edit_course"),
    path('edit_course_save', HodViews.EditCourseSave, name="edit_course_save"),

    path('add_subject', HodViews.AddSubject, name="add_subject"),
    path('add_subject_save', HodViews.AddSubjectSave, name="add_subject_save"),
    path('list_subject', HodViews.ListSubject, name="list_subject"),
    path('edit_subject/<str:subject_id>', HodViews.EditSubject, name="edit_subject"),
    path('edit_subject_save', HodViews.EditSubjectSave, name="edit_subject_save"),

    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
