import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from .models import People, Course, StudentGroup, PeopleInGroup, Schedule


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)


class PeopleType(DjangoObjectType):
    class Meta:
        model = People
        fields = ('id', 'user', 'is_teacher',)


class StudentGroupType(DjangoObjectType):
    class Meta:
        model = StudentGroup
        fields = ('id', 'name', 'course', 'start_date')


class PeopleInGroupType(DjangoObjectType):
    class Meta:
        model = PeopleInGroup
        fields = ('id', 'group', 'student')


class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        fields = ('id', 'name', 'description')


class ScheduleType(DjangoObjectType):
    class Meta:
        model = Schedule
        fields = ('class_date', 'teacher', 'group')


class Query(graphene.ObjectType):
    user = graphene.List(UserType)
    people = graphene.List(PeopleType)
    teacher = graphene.List(PeopleType)
    student = graphene.List(PeopleType)
    course = graphene.List(CourseType)
    student_group = graphene.List(StudentGroupType)
    people_in_group_filter = graphene.List(PeopleInGroupType, group_id=graphene.String(required=True))
    people_in_group = graphene.List(PeopleInGroupType)
    schedule = graphene.List(ScheduleType)

    def resolve_people(self, info):
       result = People.objects.all()
       return result

    def resolve_teacher(self, info):
       result = People.objects.filter(is_teacher=True)
       return result

    def resolve_student(self, info):
       result = People.objects.filter(is_teacher=False)
       return result

    def resolve_student_group(self, info):
       result = StudentGroup.objects.all()
       return result

    def resolve_course(self, info):
       result = Course.objects.all()
       return result

    def resolve_user(self, info):
       result = User.objects.all()
       return result

    def resolve_people_in_group(self, info):
       result = PeopleInGroup.objects.all()
       return result

    def resolve_people_in_group_filter(self, info, group_id):
        result = PeopleInGroup.objects.filter(group_id=group_id)
        return result

    def resolve_schedule(self, info):
       result = Schedule.objects.all()
       return result

schema = graphene.Schema(query=Query)
