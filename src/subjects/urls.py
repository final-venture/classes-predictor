from django.contrib import admin
from django.urls import path, include
from .views import (subject_list_view)

app_name = 'subjects'
urlpatterns = [
    path('', subject_list_view, name='subject-list'),
    # path('<int:pk>/', SubjectDetailView.as_view(), name='subject-detail')
]
