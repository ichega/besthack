from django.db import models
from ckeditor.fields import RichTextField

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

class PartnerModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    fl = models.BooleanField(default=True,verbose_name="Физическое лицо?")
    inn = models.CharField(max_length=100, verbose_name="ИНН")
    site = models.CharField(max_length=100, verbose_name="Веб-сайт")
    description = models.CharField(max_length=100, verbose_name="Краткое описание")
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    email = models.CharField(max_length=100, verbose_name="Email")
    image = models.ImageField(null=True, verbose_name="Картинка")

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"



class TaskModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Казвание")

    partner = models.ForeignKey(PartnerModel, on_delete=models.CASCADE, verbose_name="Картнер", null=True)
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE, verbose_name="Мероприятие", null=True)
    dt = models.DateTimeField(null=True,verbose_name="Крайний срок выполнения задания")
    image = models.ImageField(null=True, verbose_name="Картинка")

    def __str__(self):
        return self.name
    class Meta():
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"



