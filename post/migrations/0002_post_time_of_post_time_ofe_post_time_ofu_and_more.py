# Generated by Django 4.2 on 2023-07-24 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time_of',
            field=models.CharField(blank=True, max_length=9999900, null=True, verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='post',
            name='time_ofe',
            field=models.CharField(blank=True, max_length=9999900, null=True, verbose_name='Бюджет'),
        ),
        migrations.AddField(
            model_name='post',
            name='time_ofu',
            field=models.CharField(blank=True, max_length=9999900, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_on',
            field=models.CharField(blank=True, max_length=9999900, null=True, verbose_name='Кинокомпания'),
        ),
    ]
