from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from core.models import Course, People


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {'people': People.objects.get(user_id=request.user.id)}
    return render(request, 'core/base.html', context)


class PeopleContextMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['people'] = People.objects.select_related().get(user_id=self.request.user.id)
        return context


class CourseList(PeopleContextMixin, ListView):
    model = Course


class CourseViewDetail(PeopleContextMixin, DetailView):
    model = Course
    pk_url_kwarg = 'course_pk'


class CourseCreateView(PeopleContextMixin, CreateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('core:course_list')


class CourseUpdateView(PeopleContextMixin, UpdateView):
    model = Course
    fields = '__all__'
    pk_url_kwarg = 'course_pk'
    template_name_suffix = '_form'
    success_url = reverse_lazy('core:course_list')


class CourseDeleteView(PeopleContextMixin, DeleteView):
    model = Course
    pk_url_kwarg = 'course_pk'
    success_url = reverse_lazy('core:course_list')
