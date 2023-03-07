from django.shortcuts import render

from courseinfo.models import Instructor, Section, Course, Semester, Student, Registration


def instructor_list_view(request):
    instructor_list = Instructor.objects.all()
    # instructor_list = Instructor.objects.none()
    return render(request, 'courseinfo/instructor_list.html', {'instructor_list': instructor_list})


def section_list_view(request):
    section_list = Section.objects.all()
    # section_list.html = Section.objects.none()
    return render(request, 'courseinfo/section_list.html', {'section_list': section_list})


def course_list_view(request):
    course_list = Course.objects.all()
    # course_list.html = Course.objects.none()
    return render(request, 'courseinfo/course_list.html', {'course_list': course_list})


def semester_list_view(request):
    semester_list = Semester.objects.all()
    # semester_list.html = Semester.objects.none()
    return render(request, 'courseinfo/semester_list.html', {'semester_list': semester_list})


def student_list_view(request):
    student_list = Student.objects.all()
    # student_list.html = Student.objects.none()
    return render(request, 'courseinfo/student_list.html', {'student_list': student_list})


def registration_list_view(request):
    registration_list = Registration.objects.all()
    # registration_list.html = Registration.objects.none()
    return render(request, 'courseinfo/registration_list.html', {'registration_list': registration_list})
