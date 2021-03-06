# Generated by Django 2.1.7 on 2019-03-30 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('dt_start', models.DateTimeField(null=True)),
                ('dt_finish', models.DateTimeField(null=True)),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='картинка')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='PartnerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('fl', models.BooleanField(default=True, verbose_name='физическое лицо?')),
                ('inn', models.CharField(max_length=100, verbose_name='инн')),
                ('site', models.CharField(max_length=100, verbose_name='веб-сайт')),
                ('description', models.CharField(max_length=100, verbose_name='краткое описание')),
                ('phone', models.CharField(max_length=100, verbose_name='телефон')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='картинка')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('dt', models.DateTimeField(null=True, verbose_name='крайний срок выполнения задания')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='картинка')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.EventModel', verbose_name='мероприятие')),
                ('partner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.PartnerModel', verbose_name='партнер')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
