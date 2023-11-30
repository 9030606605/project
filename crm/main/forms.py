from django import forms
from .models import courses,NewStudent,Demo,Student,Attendance,Test,passouts,admissionform,jopForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewStudentForm(forms.ModelForm):
    # define the foreign key relationship to the courses model
    course = forms.ModelChoiceField(queryset=courses.objects.all())

    class Meta:
        model = NewStudent
        fields = '__all__'


class courseform(forms.ModelForm):
    class Meta:
        model=courses
        fields='__all__'

class DemoForm(forms.ModelForm):
    class Meta:
        model=Demo
        fields='__all__'

class Createuser(UserCreationForm):
    is_staff = forms.BooleanField(required=False)
    #is_superuser = forms.BooleanField(required=False)
    # is_active = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ['username','email','password1','password2','is_staff']

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'present']


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['student', 'test_date', 'marks']

class PassoutsForm(forms.ModelForm):
    class Meta:
        model = passouts
        fields = ['Name', 'P_image', 'compnay', 'package', 'course']

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = admissionform
        fields = '__all__'
        widgets = {
            'DateOfjoining': forms.DateInput(attrs={'type': 'date'}),
        }

class jobform(forms.ModelForm):
    class Meta:
        model=jopForm
        fields= '__all__'

class ResumeForm(forms.Form):
    resume = forms.FileField(label='Select a resume file')       