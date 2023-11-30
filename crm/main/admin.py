from django.contrib import admin
from .models import NewStudent,courses,Demo,passouts,Student,Test,Interview,Attendance,RemovedStudent,admissionform,jopForm
# Register your models here.


admin.site.register(NewStudent)
admin.site.register(RemovedStudent)
admin.site.register(Demo)
admin.site.register(passouts)
admin.site.register(Test)
admin.site.register(Interview)
admin.site.register(Attendance)
admin.site.register(admissionform)
admin.site.register(jopForm)

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('cname', 'ctrainer', 'display_key_features')

    def display_key_features(self, obj):
        if obj.ckey:
            key_features = obj.ckey.split('. ')
            return key_features
        else:
            return []

    display_key_features.short_description = 'Key Features'


admin.site.register(courses, CoursesAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'joining_date','course']

admin.site.register(Student, StudentAdmin)

