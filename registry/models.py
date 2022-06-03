from django.db import models


# Table with foreign key (FK)
class Faculty(models.Model):
    faculty = models.CharField(max_length=50)

    def __str__(self):
        return self.faculty


# Student's gender
GENDER = (
    ("M", "M"),
    ("F", "F"),
)


class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
