# Generated by Django 3.1.1 on 2020-10-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20200915_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='priority',
            field=models.PositiveIntegerField(default=0, verbose_name='우선순위'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='content',
            field=models.TextField(blank=True, verbose_name='내용'),
        ),
    ]
