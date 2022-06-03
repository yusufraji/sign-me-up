from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "phone", "email", "gender", "faculty")
        labels = {
            "name": "Name",
            "email": "Email",
        }

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "phone": forms.TextInput(attrs={"placeholder": "Your phone"}),
            "email": forms.TextInput(attrs={"placeholder": "Your email"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["gender"].choices = [("", "Select a gender")] + list(
            self.fields["gender"].choices
        )[1:]
        self.fields["faculty"].empty_label = "Select an option"
        self.fields["email"].required = True
