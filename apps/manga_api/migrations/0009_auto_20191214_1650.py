# Generated by Django 2.2.7 on 2019-12-14 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga_api', '0008_auto_20191214_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='url'),
        ),
    ]