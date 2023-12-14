from django.contrib import admin
from django.urls import path, include
from .views import (StudentListView, StudentDetailView)

app_name = 'students'
urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail')
]
