from django.contrib import admin
from django.forms import ModelForm

from .models import People, StudentGroup, Course, PeopleInGroup, Schedule


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'is_teacher'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'course'


class PeopleInGroupForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = People.objects.filter(is_teacher=False)


@admin.register(PeopleInGroup)
class PeopleInGroupAdmin(admin.ModelAdmin):
    list_display = 'id', 'group', 'student'
    form = PeopleInGroupForm


class ScheduleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].queryset = People.objects.filter(is_teacher=True)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = 'id', 'class_date', 'teacher', 'group'
    form = ScheduleForm



