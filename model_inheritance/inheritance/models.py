from django.db import models

# Create your models here.
class ABC(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    class Meta:
        abstract = True

class StudentDetail(ABC):
    st_id = models.CharField(max_length=10)
    place = models.CharField(max_length=50)

class Dept(models.Model):
    school_name = models.CharField(max_length=20)
    department_name = models.CharField(max_length=20)

class MultiTableModel(Dept):
    st_class = models.CharField(max_length=20)
    grade = models.CharField(max_length=3)
    head_teacher = models.CharField(max_length=20)