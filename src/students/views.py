from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course

# Create your views here.
class StudentListView(ListView):
    model = Course
    template_name = 'students/student_list.html'
    paginate_by = 100

class StudentListView(DetailView):
    model = Course
    template_name = 'students/student_detail.html'
    