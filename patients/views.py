from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.
def employee_form(request):
    form = EmployeeForm()
    return render(request, 'employee_form.html', {'form':form})