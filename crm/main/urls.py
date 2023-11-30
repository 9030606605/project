from django.urls import path
from .import views

urlpatterns=[
    #home
    path('',views.create_student,name='homeurl'),
    path('activity/',views.activityfun,name='activityurl'),
    path('contact/',views.contactfun,name='contacturl'),
    path('cousedetail/<int:courses_id>/',views.course_deatil,name='courses_detail'),
    path('about/',views.aboutfun,name='abouturl'),
    path('python/',views.pythonfun,name='pythonurl'),
    path('java/',views.javafun,name='javaurl'),
    path('courses/',views.course_page,name='course_pageurl'),

    #admin
    path('staff/',views.adminpage,name='adminpageurl'),
    path('course/<int:course_id>/', views.students_by_course, name='courseurl'),
    path('student/<int:student_id>/remove/', views.remove_student, name='remove_student'),
    path('move/<int:record_id>/',views.movefun,name='moveurl'),
    path('demo/',views.demofun,name='demourl'),
    path('remove/',views.demo_removefun,name='demo_removeurl'),
    path('demo/register/',views.register_demo, name='register_demo'),
    # path('registration/',views.regfun,name='regurl'),
    path('addstudent/',views.add_student,name='addstudenturl'),
    path('mark_attendance/', views.mark_attendance, name='mark-attendance'),
    path('upload-test-data/',views.upload_test_data, name='upload_test_data'),
    path('upload-attendance-data/',views.upload_attendance_data,name='upload_attendance'),
    path('upload-interview-data/',views.upload_interview_data,name='upload_interview'),
    ###
    #admin_student view
    ###
    path('students/',views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_details, name='student_details'),
    path('students/<int:student_id>/tests/',views.student_tests, name='student_tests'),
    path('students/<int:student_id>/interviews/',views.student_interviews, name='student_interviews'),
    path('students/<int:student_id>/attendance/',views.student_attendance, name='student_attendance'),
    path('students/<int:student_id>/resume/',views.student_ressume_view,name='student_resume_view'),
    path('add-student/', views.passout_student, name='passout_student'),
    path('signup/',views.registerUser,name='signupurl'),

    #login
    path('login/',views.loginfun,name='loginurl'),
    path('logout/',views.logoutfun,name='logouturl'),
    #student page
    path('studenthome',views.student_home,name='studenthomeurl'),
    path('test/',views.weekly_test,name='testurl'),
    path('interview/',views.interview,name='interviewurl'),
    path('attadance/',views.attadance,name='attadanceurl'),
    #search
    path('coursesearch/',views.course_search,name='course_searchurl'),
    path('demosearch/',views.demo_search,name='demo_searchurl'),
    path('add_user/',views.add_user,name='add_user'),
    # Success URL
    path('success/',views.success, name='success_url'),
    path('change_password/', views.change_password, name='change_password'),
    path('change_password/done/', views.password_change_done, name='password_change_done'),
    path('form/',views.formfun,name='formurl'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('pcourse/',views.Md_courselist,name='pcourse'),
    path('md_passout/<int:course_id>/', views.passout_list, name='passout_list'),
    #student perfomance
    path('attendance1/', views.attendance_view, name='attendance'),
    path('student/test/graph/', views.student_test_graph, name='student_test_graph'),
    path('interview_graph/', views.student_interview_graph, name='interview_graph'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'), 
    path('admissionFrom/',views.admission_form_view,name='admissionform'),
    path('admsucces/',views.admsucces,name='admsuccess'),
    path('jobform/',views.job_form,name='job_form'),
    path('update-resume/', views.update_resume, name='update_resume'),
    path('view_resume/',views.studentresume,name='view_resume'),

]