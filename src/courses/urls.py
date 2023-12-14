from django.contrib import admin
from django.urls import path, include
from .views import (StudentListView, StudentDetailView, SubjectListView, SubjectDetailView, home_view)

app_name = 'courses'
urlpatterns = [
    path('', home_view, name='home'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('subjects/<str:subject>/', SubjectDetailView.as_view(), name='subject-detail'),
]
