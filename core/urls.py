from rest_framework.routers import DefaultRouter
from django.urls import path, include
import core.views as views
from . import forms
from .viewset import CourseItemViewSet, PeopleItemViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'core'

router = DefaultRouter()
router.register('course', CourseItemViewSet)
router.register('people', PeopleItemViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('peopleingroup', views.PeopleInGroupList.as_view(), name='peopleingroup_list'),
    path('course', views.CourseList.as_view(), name='course_list'),
    path('course/<int:course_pk>', views.CourseViewDetail.as_view(), name='course'),
    path('course/delete/<int:course_pk>', views.CourseDeleteView.as_view(), name='course_delete'),
    path('course/edit/<int:course_pk>', views.CourseUpdateView.as_view(), name='course_edit'),
    path('course/create', views.CourseCreateView.as_view(), name='course_create'),
    path('contact', forms.ContactFormView.as_view(), name='contact'),

    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
