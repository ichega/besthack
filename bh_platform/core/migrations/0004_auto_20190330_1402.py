# Generated by Django 2.1.7 on 2019-03-30 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_eventmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnermodel',
            name='description',
            field=models.CharField(max_length=100, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='partnermodel',
            name='email',
            field=models.CharField(max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='partnermodel',
            name='inn',
            field=models.CharField(max_length=100, null=True, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='partnermodel',
            name='phone',
            field=models.CharField(max_length=100, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='partnermodel',
            name='site',
            field=models.CharField(max_length=100, null=True, verbose_name='Веб-сайт'),
        ),
    ]
