"""TrainingSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
import core.views as views

app_name = 'core'


urlpatterns = [
    path('', views.index, name='home'),
    path('course', views.CourseList.as_view(), name='course_list'),
    path('course/<int:course_pk>', views.CourseViewDetail.as_view(), name='course'),
    path('course/delete/<int:course_pk>', views.CourseDeleteView.as_view(), name='course_delete'),
    path('course/edit/<int:course_pk>', views.CourseUpdateView.as_view(), name='course_edit'),
    path('course/create', views.CourseCreateView.as_view(), name='course_create'),
]
