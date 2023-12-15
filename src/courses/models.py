from django.db import models
from django.urls import reverse
# Create your models here.

class Course(models.Model):
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    grad_year = models.IntegerField(blank=True, null=True)
    subject1 = models.CharField(max_length=32, blank=True, null=True)
    subject2 = models.CharField(max_length=32, blank=True, null=True)
    subject3 = models.CharField(max_length=32, blank=True, null=True)
    subject4 = models.CharField(max_length=32, blank=True, null=True)
    subject5 = models.CharField(max_length=32, blank=True, null=True)
    subject6 = models.CharField(max_length=32, blank=True, null=True)
    subject7 = models.CharField(max_length=32, blank=True, null=True)
    subject8 = models.CharField(max_length=32, blank=True, null=True)
    subject9 = models.CharField(max_length=32, blank=True, null=True)
    subject10 = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'
    
    def get_student_subjects(self):
        student_subjects = []
        for i in range(1,11):
            new_subject = eval(f'self.subject{i}')
            if new_subject:
                student_subjects.append(new_subject)
        return student_subjects
    