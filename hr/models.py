from django.db import models
from django.utils import timezone


# class Compensation(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#
class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.phone


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class EmployeeQuerySet(models.QuerySet):
    def get_experience(self):
        return self.filter(work_experience__gt=3)

    def get_not_experience(self):
        return self.filter(work_experience__lte=3)


class CustomManager(models.Manager):
    def get_queryset(self):
        return EmployeeQuerySet(self.model, using=self._db)

    def get_experience(self):
        return self.get_queryset().get_experience()

    def get_not_experience(self):
        return self.get_queryset().get_not_experience()


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.SmallIntegerField(null=True)
    created = models.DateTimeField(default=timezone.now)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True


class Employee(Person):
    about = models.CharField(max_length=10000)
    work_experience = models.SmallIntegerField(default=0, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, null=True)
    # compensations = models.ManyToManyField(Compensation)

    objects = models.Manager()
    persons = CustomManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Trainee(Person):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'