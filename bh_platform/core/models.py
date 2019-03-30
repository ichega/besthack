from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
class BaseProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, verbose_name="Краткое описание", null=True, blank=True)
    phone = models.CharField(max_length=100, verbose_name="Телефон", null=True, blank=True)
    email = models.CharField(max_length=100, verbose_name="Email", null=True, blank=True)
    image = models.ImageField(null=True, verbose_name="Картинка", blank=True)
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name



class VolunteerProfile(BaseProfile):

    class Meta:
        verbose_name = "Профиль волонтера"
        verbose_name_plural = "Профили волонтеров"


class StaffProfile(BaseProfile):
    class Meta:
        verbose_name = "Профиль сотрудника"
        verbose_name_plural = "Профили сотрудников"

class ManagerProfile(BaseProfile):
    class Meta:
        verbose_name = "Профиль организатора"
        verbose_name_plural = "Профили организаторов"


class PartherProfile(BaseProfile):
    is_phys = models.BooleanField(default=True, verbose_name="Физическое лицо?", blank=True)
    inn = models.CharField(max_length=100, verbose_name="ИНН", null=True, blank=True)
    site = models.CharField(max_length=100, verbose_name="Веб-сайт", null=True, blank=True)

    class Meta:
        verbose_name = "Профиль партнера"
        verbose_name_plural = "Профили партнеров"


class EventModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = RichTextField(config_name='awesome_ckeditor', null=True)
    dt_start = models.DateTimeField(null=True, verbose_name="Начало")

    dt_finish = models.DateTimeField(null=True, verbose_name="Конец")
    image = models.ImageField(null=True, verbose_name="Картинка")
    owner = models.ForeignKey(ManagerProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class TaskModel(models.Model):
    perfomer = models.ForeignKey(BaseProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Название")

    partner = models.ForeignKey(PartherProfile, on_delete=models.DO_NOTHING, verbose_name="Партнер", null=True,
                                blank=True)
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE, verbose_name="Мероприятие")
    deadline = models.DateTimeField(null=True, verbose_name="Deadline")
    image = models.ImageField(null=True, verbose_name="Картинка")

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
