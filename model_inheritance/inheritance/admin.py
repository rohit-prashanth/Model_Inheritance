"""from django.contrib import admin
from .models import StudentDetail,MultiTableModel
# Register your models here.
@admin.register(StudentDetail)
class AdminStudentDetails(admin.ModelAdmin):
    list_display = ['st_id','name','age','place']

@admin.register(MultiTableModel)
class AdminMultipleTable(admin.ModelAdmin):
    list_display = ['school_name','department_name'
                    'st_class','grade','head_teacher']"""