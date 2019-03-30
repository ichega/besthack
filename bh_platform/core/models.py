from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Название")
    is_phys = models.BooleanField(default=True, verbose_name="Физическое лицо?", blank=True)
    is_pathner = models.BooleanField(default=True, verbose_name="Партнер?", blank=True)
    is_volon = models.BooleanField(default=False, verbose_name="Волонтер?", blank=True)
    is_staff = models.BooleanField(default=False, verbose_name="Сотрудник", blank=True)
    is_owner = models.BooleanField(default=False, verbose_name="Организатор", blank=True)
    inn = models.CharField(max_length=100, verbose_name="ИНН", null=True, blank=True)
    site = models.CharField(max_length=100, verbose_name="Веб-сайт", null=True, blank=True)

    description = models.CharField(max_length=100, verbose_name="Краткое описание", null=True, blank=True)
    phone = models.CharField(max_length=100, verbose_name="Телефон", null=True, blank=True)
    email = models.CharField(max_length=100, verbose_name="Email", null=True, blank=True)
    image = models.ImageField(null=True, verbose_name="Картинка", blank=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class EventModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
    dt_start = models.DateTimeField(null=True, verbose_name="Начало")

    dt_finish = models.DateTimeField(null=True, verbose_name="Конец")
    image = models.ImageField(null=True, verbose_name="Картинка", blank=True)
    owner = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class TaskModel(models.Model):
    perfomer = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="perfomer")
    name = models.CharField(max_length=100, verbose_name="Название")
    description = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
    partner = models.ForeignKey(ProfileModel, on_delete=models.DO_NOTHING, verbose_name="Партнер", null=True,
                                blank=True, related_name="partner")
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE, verbose_name="Мероприятие")
    deadline = models.DateTimeField(null=True, verbose_name="Deadline", blank=True)


    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
