from django_filters.rest_framework import FilterSet, DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.viewsets import ModelViewSet

from core.models import Course, People, Schedule
from core.serializer import CourseSerializer, PeopleSerializer, ScheduleSerializer


class PeopleFilter(FilterSet):
    # description = CharFilter(method=filter_icontains)
    # task_executor_name = CharFilter(method=filter_icontains, field_name='task_executor__name')

    class Meta:
        model = People
        fields = ['is_teacher']


class AppPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return bool(request.user and request.user.is_authenticated)


class CourseItemViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AppPermission]


class PeopleItemViewSet(ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    filterset_class = PeopleFilter
    filter_backends = (DjangoFilterBackend,)

    permission_classes = [IsAuthenticated]


class ScheduleItemViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    # permission_classes = [AppPermission]