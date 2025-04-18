# app/management/commands/generate_fake_data.py

from django.core.management.base import BaseCommand
from faker import Faker
from app.models import Employee, Performance

class Command(BaseCommand):
    help = 'Generate synthetic employee records'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(5):  # Generate 5 employees
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.email(),
                position=fake.job(),
                department=fake.word(),
                hire_date=fake.date_this_decade(),
                salary=fake.random_number(digits=5)
            )

            # Create performance records for each employee
            for _ in range(3):  # Assume 3 performance records per employee
                Performance.objects.create(
                    employee=employee,
                    review_date=fake.date_this_year(),
                    score=fake.random_int(min=1, max=5),
                    comments=fake.sentence()
                )

        self.stdout.write(self.style.SUCCESS('Successfully generated synthetic data'))