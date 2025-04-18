from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)  # e.g., 'Present', 'Absent'
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    score = models.IntegerField()  # e.g., 1 to 5
    comments = models.TextField()

    def __str__(self):
        return f"{self.employee.name} - {self.review_date}"

class Department(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='managed_departments')

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    employees = models.ManyToManyField(Employee, related_name='projects')

    def __str__(self):
        return self.name
