# Generated by Django 2.2.7 on 2019-11-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MangaPoster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Обложка')),
            ],
        ),
        migrations.AlterModelOptions(
            name='manga',
            options={'verbose_name': 'Манга', 'verbose_name_plural': 'Манги'},
        ),
        migrations.AddField(
            model_name='manga',
            name='images',
            field=models.ManyToManyField(related_name='Обложки', to='profile_api.MangaPoster'),
        ),
    ]
