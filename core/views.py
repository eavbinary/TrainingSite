from django.contrib.auth.models import User
from django.forms import Form, CharField, Textarea, EmailField
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
import django_rq

from core.models import Course, People
from core.tasks import send_mail_rq



def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {'people': People.objects.get(user_id=request.user.id)}
    return render(request, 'core/base.html', context)


class PeopleContextMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['people'] = People.objects.get(user_id=self.request.user.id)
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


class ContactForm(Form):
    subject = CharField(max_length=100)
    sender = EmailField()
    message = CharField(widget=Textarea)

    def send_email(self):
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        address = self.cleaned_data['sender']
        line = '-' * 20

        # Письмо администратору
        admin_email = User.objects.get(is_superuser=True, email__contains='@').email
        job = django_rq.enqueue(send_mail_rq, admin_email, f'Запрос от {address}',
                                f'Тема: {subject}\n{line}\n{message}')
        # Письмо пользователю
        job = django_rq.enqueue(send_mail_rq, address, f'Ваш запрос на TrainingSite принят',
                                f'Тема: {subject}\n{line}\n{message}')


class ContactFormView(FormView):
    template_name = 'core\contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


