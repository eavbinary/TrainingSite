from django.contrib.auth import get_user_model
from django.db import models


class People(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT, null=False,
                                verbose_name='Учетная запись')
    is_teacher = models.BooleanField(verbose_name='Преподавтель')

    class Meta:
        verbose_name = 'Участник сообщества'
        verbose_name_plural = 'Участники сообщества'

    def __str__(self):
        return f'{self.user}'


class Course(models.Model):
    name = models.CharField(max_length=120, default='', null=False, blank=False,
                            verbose_name='Наименование')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'{self.name}'


class StudentGroup(models.Model):
    name = models.CharField(max_length=120, default='', null=False, blank=False,
                            verbose_name='Наименование')
    course = models.ForeignKey(Course, on_delete=models.PROTECT,
                               verbose_name='Курс')
    start_date = models.DateField(null=False, default='2021-01-01',
                                  verbose_name='Дата начала')

    class Meta:
        verbose_name = 'Группа учащегося'
        verbose_name_plural = 'Группы учащихся'

    def __str__(self):
        return f'{self.name}({self.course})'


class PeopleInGroup(models.Model):
    group = models.ForeignKey(StudentGroup, on_delete=models.PROTECT,
                              verbose_name='Группа')
    student = models.ForeignKey(People, on_delete=models.PROTECT,
                                verbose_name='Студент')

    class Meta:
        verbose_name = 'Состав группы'
        verbose_name_plural = 'Составы групп'

    def __str__(self):
        return f'{self.group}'


class Schedule(models.Model):
    class_date = models.DateTimeField(null=False,verbose_name='Дата занятия')
    teacher = models.ForeignKey(People, on_delete=models.PROTECT,
                                verbose_name='Преподавтель')
    group = models.ForeignKey(StudentGroup, on_delete=models.PROTECT,
                              verbose_name='Группа')

    class Meta:
        verbose_name = 'Рассписание занятия'
        verbose_name_plural = 'Рассписание'

    def __str__(self):
        return f'{self.group}({self.teacher})-{self.class_date}'

