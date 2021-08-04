from django.shortcuts import render
from .models import StudentDetail,MultiTableModel
# Create your views here.
def home(request):
    obj = StudentDetail.objects.all()
    obj1 = MultiTableModel.objects.all()
    return render(request,'home.html',{'obj':obj,'obj1':obj1})

