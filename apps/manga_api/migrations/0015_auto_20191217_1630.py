# Generated by Django 2.2.7 on 2019-12-17 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga_api', '0014_auto_20191217_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='rating',
            field=models.FloatField(default=0, verbose_name='Rating'),
        ),
    ]
