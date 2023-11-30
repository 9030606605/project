from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


# Create your models here.


class courses(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=20)
    cdesc=models.TextField(null=True)
    image= models.ImageField(upload_to='images/',null=True)
    ctrainer=models.CharField(max_length=20,null=True)
    ckey=models.TextField(null=True)
    c_deatils=models.TextField(null=True)

    def __str__(self) -> str:
        return self.cname

class NewStudent(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]   
    
    nstdName = models.CharField(max_length=20)
    nmail = models.EmailField()
    nmobile = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    graduation = models.CharField(max_length=50)
    course = models.ForeignKey(courses, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) -> str:
        return self.nstdName

class RemovedStudent(models.Model):
    nstdName = models.CharField(max_length=20)
    nmail = models.EmailField()
    nmobile = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    graduation = models.CharField(max_length=50)
    course = models.ForeignKey(courses, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.nstdName
    
class Demo(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    graduation = models.CharField(max_length=50)
    course = models.ForeignKey(courses, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], default='No')


    def __str__(self):
        return self.Name
    
class passouts(models.Model):
    Name=models.CharField(max_length=20)
    P_image=models.ImageField(upload_to='images/',null=True)
    compnay=models.CharField(max_length=30)
    package=models.CharField(max_length=20)
    course=models.ForeignKey(courses,on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.Name

# @receiver(post_save,sender=User)
# def sendmail(sender,instance,created,**kwargs):
#     print('Sending Email')
#     if created:
#         recipient=[instance.email]
#         subject='Thank you for Registering into Vcube Software Solutions PVT.LTD'
#         message='''your username and password is {} \n {}'''.format(instance.username,instance.password)
#         # message=f'Your UserName:{instance.username}\n Your Password :{instance:password}'
#         send_mail(subject,message,'shivayadav12088@gmail.com',recipient)
#         print('Email sent Successfully')
# post_save.connect(sendmail,sender=User,)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admission_number = models.CharField(max_length=10,null=True)  # New field for admission number
    joining_date = models.DateField()
    image = models.ImageField(upload_to='images/', null=True)
    actual_fees = models.DecimalField(max_digits=8, decimal_places=2)
    fees_paid = models.DecimalField(max_digits=8, decimal_places=2)
    resume = models.FileField(upload_to='resumes/',null=True,blank=True)
    course = models.ForeignKey(courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def balance(self):
        return self.actual_fees - self.fees_paid
    

class Test(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test_date = models.DateField()
    marks = models.DecimalField(max_digits=8, decimal_places=2, validators=[MaxValueValidator(100)])

    def __str__(self):
        return f"Test: {self.pk} - Student: {self.student.user.username}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"Attendance: {self.pk} - Student: {self.student.user.username}"


class Interview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    interview_date = models.DateField()
    present = models.BooleanField(default=False)
    performance = models.DecimalField(max_digits=4, decimal_places=2,validators=[MaxValueValidator(10)],null=True)
    marks=models.DecimalField(max_digits=8,decimal_places=2,validators=[MaxValueValidator(10)],null=True)

    def __str__(self):
        return f"Interview: {self.pk} - Student: {self.student.user.username}"

class admissionform(models.Model):
    Email=models.EmailField(unique=True)
    Name=models.CharField(max_length=30)
    Mobile=models.CharField(max_length=12)
    Alternate_Mobile=models.CharField(max_length=12)
    course=models.ForeignKey(courses,on_delete=models.CASCADE)
    T_Chocies=[
        ('Mr.Srinivas','Mr.Srinivas'),
        ('Mr.Madhukar','Mr.Madhukar'),
        ('Mr.Manohar','Mr.Manohar'),
        ('Mr.Suresh','Mr.Suresh'),
        ('Mr.PVR','Mr.PVR'),
        ('O', 'Other'),
    ]
    Tranier = models.CharField(max_length=20, choices=T_Chocies)
    Mode_of_Traning=models.CharField(max_length=10,choices=[('Offline','Offline'),('Online','Online')])
    Batch_timings=models.CharField(max_length=5)
    DateOfjoining=models.DateField()
    Batch_Number=models.CharField(max_length=5)
    Qulification=models.CharField(max_length=10)
    Work_experience=models.CharField(max_length=10)
    Experience_or_Fresher=models.CharField(max_length=10)
    Backlogs=models.CharField(max_length=5)
    Linked=models.CharField(max_length=50)
    Instagram=models.CharField(max_length=30)
    Image=models.ImageField(upload_to='images/',null=True)
    INTEREST_CHOICES = [
        ('EASIER', 'Because this is easier than other courses.'),
        ('INTEREST', 'I absorbed myself I am quite interested on this course.'),
        ('SUGGESTION', 'My friend suggestion or parents suggestion.'),
        ('DEMAND', 'This course have highest demand in market.'),]
    VCUBE_CHOICES = [
        ('TRAINERS', 'VCUBE have professional trainers and process is good'),
        ('TRENDING', 'VCUBE is trending institute'),
        ('FRIEND', 'My friend suggestion'),
        ('ASSISTANCE', 'Because of 100 % assistance'),
        ]
    EXPECTATIONS_CHOICES = [
        ('PLACEMENTS', '100 % placements'),
        ('KNOWLEDGE', 'Best training and best knowledge on particular course'),
        ('GUIDANCE', 'Best guidance + placement assistance'),
        ('NONE', 'No expectations'),
        ]
    WEAKNESS_CHOICES = [
        ('FEAR', 'Stage fear'),
        ('COMMUNICATION', 'Lack of communication'),
        ('KNOWLEDGE', 'Lack of subject knowledge'),
        ('ALL', 'All the above'),
        ]

    TEST_CHOICES = [('YES', 'Yes, it is'),('NO', 'No'),('UNKNOWN', 'I don’t know'),]

    MOCK_CHOICES = TEST_CHOICES

    HEAR_CHOICES = [('SOCIAL', 'Social media'),('FRIEND', 'Friends reference'),('RANDOM', 'Randomly'),]
    course_interest = models.CharField(max_length=20, choices=INTEREST_CHOICES,blank=False)
    v_cube_reason = models.CharField(max_length=20, choices=VCUBE_CHOICES,blank=False)
    expectations = models.CharField(max_length=20, choices=EXPECTATIONS_CHOICES,blank=False)
    weakness = models.CharField(max_length=20, choices=WEAKNESS_CHOICES,blank=False)
    test_importance = models.CharField(max_length=20, choices=TEST_CHOICES,blank=False)
    mock_value = models.CharField(max_length=20, choices=MOCK_CHOICES,blank=False)
    hear_about_us = models.CharField(max_length=20, choices=HEAR_CHOICES,blank=False)


class jopForm(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    #...add more CHOICES as needed

    current_city = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    #acdamic Details
    resume = models.FileField(upload_to='resumes/')
    degree_college = models.CharField(max_length=255)
    passed_out_year = models.IntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    post_graduation = models.CharField(max_length=255, null=True, blank=True)
    pg_degree_college = models.CharField(max_length=255, null=True, blank=True)
    pg_passed_out_year = models.IntegerField(null=True, blank=True)

    # profinal Details
    relevant_experience = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    reporting_person_contact = models.CharField(max_length=255, null=True, blank=True)

    
