from django.contrib import admin

from courseinfo.models import Period, Year, Semester, Section, Course, Instructor, Student, Registration

admin.site.register(Period)
admin.site.register(Year)
admin.site.register(Semester)
admin.site.register(Section)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Registration)
