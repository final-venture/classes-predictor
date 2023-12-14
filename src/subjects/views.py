from django.shortcuts import render
from ..models import Course
from django.shortcuts import get_object_or_404
from django.db import connection
from django.db.models import Q
from django.views import View
from django.views.generic import DetailView

def get_distinct_subjects():
    with connection.cursor() as cursor:
        cursor.execute(
        """
        SELECT DISTINCT subject
            FROM (
            SELECT subject1 AS subject FROM course
            UNION ALL
            SELECT subject2 AS subject FROM course
            UNION ALL
            SELECT subject3 AS subject FROM course
            UNION ALL
            SELECT subject4 AS subject FROM course
            UNION ALL
            SELECT subject5 AS subject FROM course
            UNION ALL
            SELECT subject6 AS subject FROM course
            UNION ALL
            SELECT subject7 AS subject FROM course
            UNION ALL
            SELECT subject8 AS subject FROM course
            UNION ALL
            SELECT subject9 AS subject FROM course
            UNION ALL
            SELECT subject10 AS subject FROM course
            ) AS sub;
        """
        )

        return cursor.fetchall()

def get_subject_participants(sub):
    query = Q(subject1=sub) | Q(subject2=sub) | Q(subject3=sub) | Q(subject4=sub) | Q(subject5=sub) | Q(subject6=sub) | Q(subject7=sub) | Q(subject8=sub) | Q(subject9=sub) | Q(subject10=sub)
    result_queryset = Course.objects.filter(query)
    return result_queryset

# Create your views here.
class SubjectListView(View):
    def get(self, request):
        context = {"subject_list": get_distinct_subjects()}
        return render(request, 'subjects/subject_list.html', context)

class SubjectDetailView(View):
    def get(self, request, subject):
        queryset = get_subject_participants(subject)
        context = {"queryset": queryset}
        return render(request, 'subjects/subject_detail.html', context)
