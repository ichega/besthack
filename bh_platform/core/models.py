from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class EventModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = RichTextField(config_name='awesome_ckeditor', null=True)
    dt_start = models.DateTimeField(null=True, verbose_name="Начало")

    dt_finish = models.DateTimeField(null=True, verbose_name="Конец")
    image = models.ImageField(null=True, verbose_name="Картинка")

    def __str__(self):
        return self.name
    class Meta():
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

class ProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Название")
    is_phys = models.BooleanField(default=True,verbose_name="Физическое лицо?", blank=True)
    # CHOICES = [('is_pathner', 'Партнер'),
    #            ('is_volon', 'Волонтер'),
    #            ('is_org', 'Организатор'),
    #            ('is_staff', 'Сотрудник')]
    is_pathner= models.BooleanField(default=True,verbose_name="Партнер?", blank=True)
    is_volon = models.BooleanField(default=False,verbose_name="Волонтер?", blank=True)
    is_staff = models.BooleanField(default=False,verbose_name="Сотрудник", blank=True)
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



class TaskModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Казвание")

    partner = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, verbose_name="Партнер", null=True)
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE, verbose_name="Мероприятие", null=True)
    dt = models.DateTimeField(null=True,verbose_name="Крайний срок выполнения задания")
    image = models.ImageField(null=True, verbose_name="Картинка")

    def __str__(self):
        return self.name
    class Meta():
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"



