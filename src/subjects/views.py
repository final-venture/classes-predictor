from django.shortcuts import render
from .models import Course

# Create your views here.
def subject_list_view(request):
    queryset = Course.objects.order_by().values('subject1').distinct()
    print(queryset)
    context = {"queryset": queryset}
    return render(request, 'subjects/subject_list.html', context)
