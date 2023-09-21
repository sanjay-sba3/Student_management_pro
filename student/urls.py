from django.contrib import admin
from django.urls import path
from student.views import student, user

urlpatterns = [
    path('user', user.UserViews.as_view(), name='user'),
    path('student', student.StudentViews.as_view(), name='student'),
    path('login', user.LoginViews.as_view(), name='login')
]
