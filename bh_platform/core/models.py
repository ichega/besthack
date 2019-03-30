from django.db import models

# Create your models here.

class EventModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    dt_start = models.DateTimeField(null=True)
    dt_finish = models.DateTimeField(null=True)
    image = models.ImageField(null=True, verbose_name="картинка")

    def __str__(self):
        return self.name
    class Meta():
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

class PartnerModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    fl = models.BooleanField(default=True,verbose_name="физическое лицо?")
    inn = models.CharField(max_length=100, verbose_name="инн")
    site = models.CharField(max_length=100, verbose_name="веб-сайт")
    description = models.CharField(max_length=100, verbose_name="краткое описание")
    phone = models.CharField(max_length=100, verbose_name="телефон")
    email = models.CharField(max_length=100, verbose_name="Email")
    image = models.ImageField(null=True, verbose_name="картинка")

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"



class TaskModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")

    partner = models.ForeignKey(PartnerModel, on_delete=models.CASCADE, verbose_name="партнер", null=True)
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE, verbose_name="мероприятие", null=True)
    dt = models.DateTimeField(null=True,verbose_name="крайний срок выполнения задания")
    image = models.ImageField(null=True, verbose_name="картинка")

    def __str__(self):
        return self.name
    class Meta():
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"



