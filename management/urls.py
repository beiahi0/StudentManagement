"""
URL configuration for day16 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path, include
# from app01.views import depart, user, pretty, admin, account, task, order
from management.views import account, student, sdept, course, sc
from . import views

urlpatterns = [
    path("", account.login),
    path('login/', account.login),
    path('logout/', account.logout),
    path('register/', account.register),

    #     学生信息
    path('student/list/', student.student_list),
    path('student/add/', student.student_add),
    path('student/<str:nid>/delete/', student.student_delete),
    path('student/<str:nid>/edit/', student.student_edit),

    path('sdept/list/', sdept.sdept_list),
    path('sdept/add/', sdept.sdept_add),
    path('sdept/<str:nid>/delete/', sdept.sdept_delete),
    path('sdept/<str:nid>/edit/', sdept.sdept_edit),

    path('course/list/', course.course_list),
    path('course/add/', course.course_add),
    path('course/<str:nid>/delete/', course.course_delete),
    path('course/<str:nid>/edit/', course.course_edit),

    #     学生选课表

    path('sc/list/', sc.sc_list),
    path('sc/<int:nid>/delete/', sc.sc_delete),
    path('sc/<int:nid>/edit/', sc.sc_edit),
    path('sc/add/', sc.sc_add),
]
