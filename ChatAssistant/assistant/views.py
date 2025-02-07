from django.shortcuts import render

# Create your views here.
from django.db.models import Sum
from django.shortcuts import render
from django.http import JsonResponse
from assistant.models import Employee, Department
import re

def chat_assistant(request):
    query = request.GET.get('query', '').lower()

    if not query:
        return JsonResponse({"error": "No query provided"}, status=400)
    match = re.search(r"employees in the (.+?) department", query)
    if match:
        department_name = match.group(1).capitalize()
        employees = Employee.objects.filter(department__name=department_name)
        return JsonResponse({"employees": [e.name for e in employees]})
    match = re.search(r"manager of the (.+?) department", query)
    if match:
        department_name = match.group(1).capitalize()
        department = Department.objects.filter(name=department_name).first()
        if department:
            return JsonResponse({"manager": department.manager})
        return JsonResponse({"error": "Department not found"}, status=404)
    match = re.search(r"hired after (\d{4}-\d{2}-\d{2})", query)
    if match:
        hire_date = match.group(1)
        employees = Employee.objects.filter(hire_date__gt=hire_date)
        return JsonResponse({"employees": [e.name for e in employees]})
    match = re.search(r"total salary expense for the (.+?) department", query)
    if match:
        department_name = match.group(1).capitalize()
        total_salary = Employee.objects.filter(department__name=department_name).aggregate(total=Sum('salary'))
        return JsonResponse({"total_salary": total_salary['total'] if total_salary['total'] else 0})

    return JsonResponse({"error": "Query not understood or no data found"}, status=400)


def index(request):
    return render(request, 'index.html')
