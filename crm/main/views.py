
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseNotAllowed
from .forms import NewStudentForm,courses,DemoForm,StudentForm,AttendanceForm,TestForm,PassoutsForm,Createuser,courseform,AdmissionForm,jobform,ResumeForm
from .models import NewStudent,RemovedStudent,Demo,passouts,Student,Test,Interview,Attendance,admissionform
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from datetime import datetime
import pandas as pd

def formfun(request):
    try:
        if request.method == 'POST':
            form =courseform (request.POST)
            if form.is_valid():
                form.save()
                return redirect('adminpageurl')
        else:
            form = courseform()
        return render(request, 'admin_upload/add_course.html', {'form':form})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


def create_student(request):
    try:
        course = courses.objects.all().order_by('cid')
        passout = passouts.objects.all()

        if request.method == 'POST':
            form = NewStudentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Student created successfully.')
                return redirect('homeurl')
            else:
                messages.error(request, 'Failed to create student. Please check the form data.')
        else:
            form = NewStudentForm()

        context = {
            'form': form,
            'courses': course,
            'passout': passout,
        }

        return render(request, 'main/first.html', context)
    except Exception as e:
        return HttpResponse("Error: " + str(e))


def activityfun(request):
    return render(request, 'main/our_acitivy.html')


def contactfun(request):
    return render(request, 'main/contact.html')


def aboutfun(request):
    return render(request, 'main/about_page.html')


def pythonfun(request):
    return render(request, 'courses/python.html')


def javafun(request):
    return render(request, 'courses/java.html')


def course_page(request):
    try:
        all_courses = courses.objects.all()

        context = {
            'courses': all_courses
        }

        return render(request, 'courses/courses.html', context)
    except Exception as e:
        return HttpResponse("Error: " + str(e))


def course_deatil(request, courses_id):
    try:
        course = courses.objects.get(pk=courses_id)
        return render(request, 'courses/courses_deatil.html', {'course': course})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


# demo register_demo
@user_passes_test(lambda user: user.is_staff, login_url='loginurl')
def register_demo(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            gender = request.POST['gender']
            graduation = request.POST['graduation']
            course_id = request.POST['course']

            course = courses.objects.get(cid=course_id)

            demo = Demo(Name=name, Email=email, Mobile=mobile, gender=gender, graduation=graduation, course=course)
            demo.save()

            return redirect('homeurl')

        else:
            courses_list = courses.objects.all()
            context = {'courses': courses_list}
            return render(request, 'admin/demo_registration.html', context)
    except Exception as e:
        return HttpResponse("Error: " + str(e))


# admin view
@user_passes_test(lambda user: user.is_staff, login_url='loginurl')
@login_required(login_url='loginurl')
def adminpage(request):
    try:
        course_list = courses.objects.all()
        context = {'course_list': course_list}
        return render(request, 'admin/adminpage.html', context)
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user: user.is_staff, login_url='loginurl')
def students_by_course(request, course_id):
    try:
        course = courses.objects.get(cid=course_id)
        students = NewStudent.objects.filter(course=course)
        context = {'course': course, 'students': students}
        return render(request, 'admin/students_by_course.html', context)
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user: user.is_staff, login_url='loginurl')
def remove_student(request, student_id):
    try:
        student = NewStudent.objects.get(pk=student_id)
        RemovedStudent.objects.create(
            nstdName=student.nstdName,
            nmail=student.nmail,
            nmobile=student.nmobile,
            gender=student.gender,
            graduation=student.graduation,
            course=student.course,
        )
        return render(request, 'admin/demo_remove.html', {'student': student})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user: user.is_staff, login_url='loginurl')
def movefun(request, record_id):
    try:
        add = NewStudent.objects.get(id=record_id)
        res = Demo.objects.create(Name=add.nstdName,
                                  Email=add.nmail,
                                  Mobile=add.nmobile,
                                  gender=add.gender,
                                  graduation=add.graduation,
                                  course=add.course)
        return redirect('adminpageurl')
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user: user.is_staff, login_url='loginurl')
def demofun(request):
    try:
        output = Demo.objects.order_by('-created_at')

        return render(request, 'admin/demo.html', {'res': output})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user: user.is_staff, login_url='loginurl')
def demo_removefun(request):
    try:
        remove = RemovedStudent.objects.all()

        return render(request, 'admin/demo_remove.html', {'res': remove})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


def loginfun(request):
    try:
        if request.method == 'POST':
            uname = request.POST['username']
            pwd = request.POST['pwd']
            valid_user = authenticate(username=uname, password=pwd)

            if valid_user is not None:
                login(request, valid_user)

                if valid_user.is_superuser:
                    return redirect('dashboard')

                elif valid_user.is_staff:
                    return redirect('adminpageurl')

                elif valid_user.is_active:
                    return redirect('studenthomeurl')

                else:
                    return HttpResponse('User not defined')

            else:
                error_message = 'Wrong password 🙄 Please check the password and try again..!!!!'
                login_url = reverse('loginurl')
                return render(request, 'main/login.html',
                              {'error_message': error_message, 'loginurl': login_url})

        return render(request, 'main/login.html', {'loginurl': reverse('loginurl')})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


def logoutfun(request):
    try:
        logout(request)
        return redirect('homeurl')
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user: user.is_staff, login_url='loginurl')
def add_student(request):
    try:
        std_info = StudentForm
        course = courses.objects.all()
        if request.method == 'POST':
            form = StudentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('loginurl')
            else:
                print(form.errors)

        return render(request, 'admin/add_student.html', {'form': std_info, 'course': course})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


def student_home(request):
    try:
        student = request.user.student
        tests = Test.objects.filter(student=student)
        attendances = Attendance.objects.filter(student=student)
        interviews = Interview.objects.filter(student=student)

        return render(request, 'student/studenthome.html',
                      {'student': student, 'tests': tests, 'attendances': attendances, 'interviews': interviews})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user: user.is_active, login_url='loginurl')
@login_required
def weekly_test(request):
    try:
        student = request.user.student
        tests = Test.objects.filter(student=student)

        return render(request, 'student/test.html', {'tests': tests, 'student': student})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user: user.is_active, login_url='loginurl')
def interview(request):
    try:
        student = request.user.student
        interview = Interview.objects.filter(student=student)
        return render(request, 'student/interview.html', {'student': student, 'interview': interview})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user: user.is_active, login_url='loginurl')
def attadance(request):
    try:
        student = request.user.student
        attadance = Attendance.objects.filter(student=student)
        return render(request, 'student/attadance.html', {'student': student, 'attadance': attadance})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


def course_search(request):
    try:
        if request.method == 'POST':
            search_query = request.POST['word']
            course = courses.objects.filter(cname__icontains=search_query)
            return render(request, 'main/search.html', {'courses': course, 'search_query': search_query})

        return render(request, 'main/search.html')
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user: user.is_staff, login_url='loginurl')
def demo_search(request):
    try:
        if request.method == 'POST':
            t = request.POST['search']
            results = Demo.objects.filter(Name__icontains=t)
            return render(request, 'admin/demo_search.html', {'res': results})
        return render(request, 'admin/demo_search.html')
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user: user.is_staff, login_url='loginurl')
def add_user(request):
    try:
        if request.method == 'POST':
            record_id = request.POST.get('record_id')
            demo = Demo.objects.get(id=record_id)

            username = demo.Name.lower().replace(" ", "")

            password = User.objects.make_random_password()



            message = f'Thank you for Registering into VCube Software Solutions Pvt.Ltd.\n\n'
            message += f'Username: {username}\nPassword: {password}\n\n'
            message += f'Please keep your Credentials Confidential and change your password for security purposes.'

            try:
                send_mail(
                    'Your Account Details',
                    message,
                    'ukumar.ch@gmail.com',
                    [demo.Email],
                    fail_silently=False,
                )
                demo.status = 'Yes'
            except Exception as e:
                demo.status = 'No'

            user = get_user_model().objects.create(
                username=username,
                password=make_password(password),
                email=demo.Email
            )

            demo.user = user
            demo.save()

            return redirect('success_url')

        return HttpResponseNotAllowed(['POST'])
    except Exception as e:
        return HttpResponse("Error: " + str(e))

@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
def success(request):
    try:
        return render(request, 'admin/success.html')
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user:user.is_active,login_url='loginurl')
def change_password(request):
    try:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password changed successfully.')
                return redirect('password_change_done')
            else:
                messages.error(request, 'Failed to change password. Please check the form data.')
        else:
            form = PasswordChangeForm(request.user)

        return render(request, 'student/change_password.html', {'form': form})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


def password_change_done(request):
    try:
        return render(request, 'student/password_change_done.html')
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
def mark_attendance(request):
    try:
        if request.method == 'GET':
            students = Student.objects.all()
            return render(request, 'admin/add_attendance.html', {'students': students})

        if request.method == 'POST':
            attendance_date = datetime.strptime(request.POST['attendance_date'], '%Y-%m-%d').date()
            student_ids = request.POST.getlist('student_ids[]')

            for student_id in student_ids:
                attendance_value = request.POST.get('attendance_' + student_id)
                student = Student.objects.get(pk=student_id)
                attendance, created = Attendance.objects.get_or_create(student=student, date=attendance_date)
                attendance.present = attendance_value == 'present'
                attendance.save()

            return redirect('mark-attendance')

        return HttpResponse("Something went wrong.")
    except Exception as e:
        return HttpResponse("Error: " + str(e))


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
import calendar

@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
def upload_test_data(request):
    try:
        if request.method == 'POST':
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)

            for index, row in df.iterrows():
                admission_number = row['admission_number']
                test_date = row['test_date']
                marks = row['marks']

                student = Student.objects.get(admission_number=admission_number)

                test = Test(student=student, test_date=test_date, marks=marks)
                test.save()

            return render(request, 'admin_upload/test_success.html')

        return render(request, 'admin_upload/test_upload.html')
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
def upload_attendance_data(request):
    try:
        if request.method == 'POST':
            attendance_file = request.FILES['attendance_file']
            df = pd.read_excel(attendance_file)

            attendance_list = []

            for index, row in df.iterrows():
                admission_number = row['admission_number']
                date = row['date']
                present_value = row['present']

                if present_value == 'Yes':
                    present = True
                elif present_value == 'No':
                    present = False
                else:
                    continue

                try:
                    student = Student.objects.get(admission_number=admission_number)
                except Student.DoesNotExist:
                    continue

                attendance = Attendance(student=student, date=date, present=present)
                attendance_list.append(attendance)

            Attendance.objects.bulk_create(attendance_list)

            return render(request, 'admin_upload/test_success.html')

        return render(request, 'admin_upload/attendance_upload.html')
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
def upload_interview_data(request):
    try:
        if request.method == 'POST':
            interview_file = request.FILES['interview_file']
            df = pd.read_excel(interview_file)

            for index, row in df.iterrows():
                admission_number = row['admission_number']
                interview_date = row['interview_date']
                performance = row['performance']
                marks = row['marks']
                present_value = row['present']

                if present_value == 'Yes':
                    present = True
                elif present_value == 'No':
                    present = False
                else:
                    continue

                try:
                    student = Student.objects.get(admission_number=admission_number)
                except Student.DoesNotExist:
                    continue

                interview = Interview(student=student, interview_date=interview_date, performance=performance, marks=marks, present=present)
                interview.save()

            return render(request, 'admin_upload/test_success.html')

        return render(request, 'admin_upload/interview_upload.html')
    except Exception as e:
        return HttpResponse("Error: " + str(e))



@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
def student_list(request):
    try:
        students = Student.objects.all()
        context = {
            'students': students
        }
        return render(request, 'admin_view/student_list.html', context)
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
def passout_student(request):
    try:
        course = courses.objects.all()
        if request.method == 'POST':
            form = PassoutsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        else:
            form = PassoutsForm()

        context = {
            'form': form,
            'courses': course
        }
        return render(request, 'admin_upload/passout_student.html', context)
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
def student_details(request, student_id):
    try:
        student = get_object_or_404(Student, id=student_id)
        context = {
            'student': student
        }
        return render(request, 'admin_view/student_details.html', context)
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
def student_tests(request, student_id):
    try:
        student = get_object_or_404(Student, id=student_id)
        tests = Test.objects.filter(student=student)
        context = {
            'student': student,
            'tests': tests
        }
        return render(request, 'admin_view/student_tests.html', context)
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
def student_interviews(request, student_id):
    try:
        student = get_object_or_404(Student, id=student_id)
        interviews = Interview.objects.filter(student=student)
        context = {
            'student': student,
            'interviews': interviews
        }
        return render(request, 'admin_view/student_interviews.html', context)
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
def student_attendance(request, student_id):
    try:
        student = get_object_or_404(Student, id=student_id)
        attendance = Attendance.objects.filter(student=student)
        context = {
            'student': student,
            'attendance': attendance
        }
        return render(request, 'admin_view/student_attendance.html', context)
    except Exception as e:
        return HttpResponse("Error: " + str(e))

@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
def student_ressume_view(request,student_id):
    try:
        student = get_object_or_404(Student, id=student_id)
        context = {
            'student': student,
        }
        return render (request,'admin_view/student_ressume_view.html', context)
    except Exception as e:
        return HttpResponse("Error: "+ str(e))
        

@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
@login_required(login_url='loginurl')
def registerUser(request):
    try:
        form = Createuser()
        if request.method == 'POST':
            obj = Createuser(request.POST)
            if obj.is_valid():
                obj.save()
                return render(request, 'admin/success.html')
            else:
                print(obj.errors)
        return render(request, 'admin/create_staff.html', {'form': form})
    except Exception as e:
        return HttpResponse("Error: " + str(e))
from django.shortcuts import render
from django.db.models import Count
from datetime import datetime, timedelta

@user_passes_test(lambda user:user.is_superuser,login_url='loginurl')
def dashboard(request):
    try:
        # Get the count of students for each model
        new_students_count = NewStudent.objects.count()
        removed_students_count = RemovedStudent.objects.count()
        demo_count = Demo.objects.count()

        # Calculate the current date
        current_date = datetime.now().date()

        context = {
            'new_students_count': new_students_count,
            'removed_students_count': removed_students_count,
            'demo_count': demo_count,
            'current_date': current_date
        }
        return render(request, 'superuser/dashboard.html', context)
    except Exception as e:
        return HttpResponse("Error: " + str(e))


#student performance

from django.db.models.functions import TruncMonth, TruncWeek
from django.db.models import Count,Max
from .models import Attendance
from decimal import Decimal
import json

@user_passes_test(lambda user:user.is_active,login_url='loginurl')
def student_dashboard(request):
    try:
        student = request.user.student

        # Attendance Pie Chart data
        present_count = Attendance.objects.filter(student=student, present=True).count()
        absent_count = Attendance.objects.filter(student=student, present=False).count()
        attendance_labels = ['Present', 'Absent']
        attendance_data = [present_count, absent_count]
        attendance_colors = ['#36a64f', '#ff5a5f']

        test_data = []  

        return render(request, 'student/dashboard.html', {
            'attendance_labels': attendance_labels,
            'attendance_data': attendance_data,
            'attendance_colors': attendance_colors,
            'test_data': test_data,
            'student':student,
        })
    except Exception as e:
        return HttpResponse("Error: " + str(e))


from django.db.models.functions import TruncMonth, TruncWeek
from django.db.models import Count
from django.utils.timezone import datetime, timedelta

@user_passes_test(lambda user:user.is_active,login_url='loginurl')
def attendance_view(request):
    try:
        student = request.user.student
        present_count = Attendance.objects.filter(student=student, present=True).count()
        absent_count = Attendance.objects.filter(student=student, present=False).count()
        attendance_labels = ['Present', 'Absent']
        attendance_data = [present_count, absent_count]
        attendance_colors = ['#36a64f', '#ff5a5f']

        interval = request.GET.get('interval')  # 'monthly' or 'weekly'
        if interval == 'monthly':
            attendance = Attendance.objects.filter(student=student).annotate(month=TruncMonth('date')).values('month').annotate(present_count=Count('pk')).order_by('month')
        elif interval == 'weekly':
            start_date = datetime.now().date() - timedelta(days=6)
            attendance = Attendance.objects.filter(student=student, date__gte=start_date).annotate(week=TruncWeek('date')).values('week').annotate(present_count=Count('pk')).order_by('week')
        else:
            attendance = Attendance.objects.filter(student=student).annotate(month=TruncMonth('date')).values('month').annotate(present_count=Count('pk')).order_by('month')

        return render(request, 'student/attendance_graph.html', {
            'attendance': attendance,
            'attendance_labels': attendance_labels,
            'attendance_data': attendance_data,
            'attendance_colors': attendance_colors,
            'student': student,
        })
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user:user.is_active,login_url='loginurl')
def student_test_graph(request):
    try:
        student = request.user.student
        tests = Test.objects.filter(student=student)

        test_data = []
        for test in tests:
            test_data.append({
                'num_tests': test.pk,
                'marks': float(test.marks),
                'test_date': test.test_date.strftime('%Y-%m-%d')
            })

        return render(request, 'student/student_test_graph.html', {'test_data': json.dumps(test_data),'student':student})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)
    
@user_passes_test(lambda user:user.is_active,login_url='loginurl')
def student_interview_graph(request):
    try:
        student = request.user.student
        interviews = Interview.objects.filter(student=student)

        interview_data = []
        max_marks_interview = None
        max_perf_interview = None
        max_marks = 0.0
        max_perf = 0.0

        for interview in interviews:
            marks = float(interview.marks) if interview.marks is not None else 0.0
            performance = float(interview.performance) if interview.performance is not None else 0.0
            interview_data.append({
                'interview_id': interview.pk,
                'date': interview.interview_date.strftime('%Y-%m-%d'),
                'performance': performance,
                'marks': marks
            })

            if marks > max_marks:
                max_marks = marks
                max_marks_interview = interview

            if performance > max_perf:
                max_perf = performance
                max_perf_interview = interview

        json_data = json.dumps(interview_data, cls=DecimalEncoder)
        return render(request, 'student/interview_graph.html', {
            'interview_data': json_data,
            'student': student,
            'max_marks_interview': max_marks_interview,
            'max_perf_interview': max_perf_interview
        })
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user:user.is_superuser,login_url='loginurl')
def Md_courselist(request):
    try:
        course=courses.objects.all()
        return render (request,'superuser/course_list.html',{'courses':course})
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@user_passes_test(lambda user:user.is_superuser,login_url='loginurl')
def passout_list(request, course_id):
    try:
        course = courses.objects.get(cid=course_id)
        passout = passouts.objects.filter(course=course)
        return render(request,'superuser/passout_list.html', {'course': course, 'passouts': passout})
    except Exception as e:
        return HttpResponse("Error: " + str(e))
    
# def admission_form_view(request):
#     if request.method == 'POST':
#         form = AdmissionForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect('admsuccess')  # Replace 'success_page' with the URL name of the success page
#     else:
#         form = AdmissionForm()
#     return render(request, 'student/admission_form.html', {'form': form})

def admission_form_view(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        email = form.data.get('Email')
        if admissionform.objects.filter(Email__iexact=email).exists():
            messages.error(request, 'You have already filled the form.')
            return render(request, 'student/admission_form.html', {'form': form})
        elif form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully.')
            request.session['form_filled'] = True  # Setting a session variable
            return redirect('admsuccess')  # Replace 'admsuccess' with the URL name of the success page
        else:
            messages.error(request, 'There was an error with your submission.')
            return render(request, 'student/admission_form.html', {'form': form})
    else:
        if request.session.get('form_filled'):  # Checking the session variable
            return render(request, 'student/admform_alredyfilled.html')  # Replace 'already_filled.html' with your actual template
        else:
            form = AdmissionForm()
    return render(request, 'student/admission_form.html', {'form': form})
    #return render(request, 'student/exm.html')


def admsucces(request):
    return render(request,'student/admform_succes.html')

def job_form(request):
    show_form = False

    # Check if there is a fourth interview with marks greater than 7.5
    interviews = Interview.objects.filter(student=request.user.student)
    fourth_interview = interviews.filter(pk__gte=4).first()  # Get the fourth interview if exists
    if fourth_interview and fourth_interview.marks and fourth_interview.marks >= 7.5:
        show_form = True

    if request.method == 'POST':
        form = jobform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admsuccess')  # redirect to a new URL
    else:
        form = jobform()

    return render(request, 'student/job_form.html', {'form': form, 'show_form': show_form})



def update_resume(request):
    student = Student.objects.get(user=request.user)

    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            student.resume = form.cleaned_data['resume']  # Save the resume directly to the 'resume' field
            student.save()
            return redirect('admsuccess')  # Redirect to the user's dashboard after successful update

    else:
        form = ResumeForm()

    return render(request, 'student/update_resume.html', {'form': form})

def studentresume(request):
    student=request.user.student
    return render(request,'student/view_resume.html',{'student':student})