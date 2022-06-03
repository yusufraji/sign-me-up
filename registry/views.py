from django.shortcuts import redirect, render

from .forms import StudentForm
from .models import Student


def read_data(request):
    context = {"read_data": Student.objects.all()}
    return render(request, "read_data.html", context)


def data_form(request, id=None):
    if request.method == "POST":
        if id is None:
            form = StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect("/data")
    else:
        if id is None:
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, "data_form.html", {"form": form})


def delete_data(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect("/data")
