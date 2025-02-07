from django.core.management.base import BaseCommand
from assistant.models import Department, Employee
from datetime import date

class Command(BaseCommand):
    def handle(self, *args, **options):
        Department.objects.all().delete()
        Employee.objects.all().delete()

        sales = Department.objects.create(name="Sales", manager="Alice")
        engineering = Department.objects.create(name="Engineering", manager="Bob")
        marketing = Department.objects.create(name="Marketing", manager="Charlie")

        Employee.objects.create(name="Alice", department=sales, salary=50000, hire_date=date(2021, 1, 15))
        Employee.objects.create(name="Bob", department=engineering, salary=70000, hire_date=date(2020, 6, 10))
        Employee.objects.create(name="Charlie", department=marketing, salary=60000, hire_date=date(2022, 3, 20))

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
