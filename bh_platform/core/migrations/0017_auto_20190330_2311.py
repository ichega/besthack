# Generated by Django 2.1.7 on 2019-03-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_taskmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='is_partner',
            field=models.BooleanField(blank=True, default=False, verbose_name='Партнер?'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='is_pathner',
            field=models.BooleanField(blank=True, default=False, verbose_name='Партнер?'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='is_phys',
            field=models.BooleanField(blank=True, default=False, verbose_name='Физическое лицо?'),
        ),
    ]
