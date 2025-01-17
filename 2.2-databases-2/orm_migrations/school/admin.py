from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'teachers')

    def teachers(self, obj):
        return "\n".join([teacher.name for teacher in obj.teachers.all()])

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'students')

    def students(self, obj):
        return "\n".join([student.name for student in obj.students.all()])
