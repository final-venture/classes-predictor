from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course

# Create your views here.
class SubjectListView(ListView):
    model = Course
    template_name = 'subjects/subject_list.html'
    paginate_by = 100

class SubjectDetailView(DetailView):
    model = Course
    template_name = 'subjects/subject_detail.html'
    