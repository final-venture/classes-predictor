from django.contrib import admin
from django.urls import path, include
from .views import (SubjectListView, SubjectDetailView)

app_name = 'subjects'
urlpatterns = [
    path('', SubjectListView.as_view(), name='subject-list'),
    path('<str:subject>/', SubjectDetailView.as_view(), name='subject-detail')
]
