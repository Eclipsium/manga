# Generated by Django 2.2.7 on 2019-12-13 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga_api', '0007_auto_20191214_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='artists',
            field=models.ManyToManyField(blank=True, to='manga_api.MangaArtist', verbose_name='Artists'),
        ),
    ]