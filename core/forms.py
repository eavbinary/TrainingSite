import django_rq
from django.contrib.auth.models import User
from django.forms import Form, CharField, EmailField, Textarea
from django.shortcuts import get_object_or_404
from django.views.generic import FormView

from core.tasks import send_mail_rq


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
        admin_user = get_object_or_404(User, is_superuser=True, email__contains='@')
        job = django_rq.enqueue(send_mail_rq, admin_user.email, f'Запрос от {address}',
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
