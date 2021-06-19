from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.viewsets import ModelViewSet

from core.models import Course, People
from core.serializer import CourseSerializer, PeopleSerializer


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

    permission_classes = [IsAuthenticated]