from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from core.models import Course, People
from core.serializer import CourseSerializer, PeopleSerializer


class PermissionModelViewSet(ModelViewSet):
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            if self.action:
                action_func = getattr(self, self.action, {})
                action_func_kwargs = getattr(action_func, 'kwargs', {})
                permission_classes = action_func_kwargs.get('permission_classes')
            else:
                permission_classes = None

            return [permission() for permission in (permission_classes or self.permission_classes)]


class CourseItemViewSet(PermissionModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'list': [AllowAny]}


class PeopleItemViewSet(ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    permission_classes = [IsAuthenticated]