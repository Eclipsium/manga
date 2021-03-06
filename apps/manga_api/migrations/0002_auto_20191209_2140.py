# Generated by Django 2.2.7 on 2019-12-09 14:40

import apps.manga_api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manga_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MangaArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Artist name')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='MangaImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_index', models.IntegerField(verbose_name='position')),
                ('image', models.ImageField(upload_to=apps.manga_api.models.get_manga_image_path, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='MangaVolume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField(verbose_name='Volume')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Upload date')),
            ],
            options={
                'verbose_name': 'Manga volume',
                'verbose_name_plural': 'Manga volume',
            },
        ),
        migrations.AlterModelOptions(
            name='manga',
            options={'verbose_name': 'Manga', 'verbose_name_plural': 'Mangas'},
        ),
        migrations.RemoveField(
            model_name='manga',
            name='author',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='drawer',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='images',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='manga_english_name',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='manga_original_name',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='manga_russian_name',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='translation',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='volumes',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='year',
        ),
        migrations.AddField(
            model_name='manga',
            name='descriptions',
            field=models.TextField(default='123', max_length=500, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manga',
            name='english_name',
            field=models.CharField(default='123123', max_length=100, verbose_name='English title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manga',
            name='is_promoted',
            field=models.BooleanField(default=False, verbose_name='Recommended'),
        ),
        migrations.AddField(
            model_name='manga',
            name='japan_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Japan title'),
        ),
        migrations.AddField(
            model_name='manga',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to=apps.manga_api.models.get_poster_path, verbose_name='Poster'),
        ),
        migrations.AddField(
            model_name='manga',
            name='rating',
            field=models.FloatField(default=0, verbose_name='Rating'),
        ),
        migrations.AddField(
            model_name='manga',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='url'),
        ),
        migrations.RemoveField(
            model_name='manga',
            name='categories',
        ),
        migrations.AddField(
            model_name='manga',
            name='categories',
            field=apps.manga_api.models.ChoiceArrayField(base_field=models.CharField(blank=True, choices=[('art', 'арт'), ('action', 'боевик'), ('martial arts', 'боевые искусства'), ('vampire', 'вампиры'), ('harem', 'гарем'), ('gender intrigue', 'гендерная интрига'), ('heroic fantasy', 'героическое фэнтези'), ('detective', 'детектив'), ('josei', 'дзёсэй'), ('doujinshi', 'додзинси'), ('drama', 'драма'), ('game', 'игра'), ('history', 'история'), ('cyberpank', 'киберпанк'), ('kodomo', 'кодомо'), ('comedy', 'комедия'), ('maho shojo', 'махо-сёдзё'), ('mechanics', 'меха'), ('science fiction', 'научная фантастика'), ('daily routine', 'повседневность'), ('post-apocalyptic', 'постапокалиптика'), ('adventures', 'приключения'), ('psychology', 'психология'), ('romantic', 'романтика'), ('samurai action', 'самурайский боевик'), ('supernatural', 'сверхъестественное'), ('shojo', 'сёдзё'), ('shojo ai', 'сёдзё-ай'), ('shonen', 'сёнэн'), ('shonen ai', 'сёнэн-ай'), ('sport', 'спорт'), ('seinen', 'сэйнэн'), ('tragedy', 'трагедия'), ('thriller', 'триллер'), ('horror', 'ужасы'), ('fantasy', 'фэнтези'), ('school', 'школа'), ('etti', 'этти'), ('yuri', 'юри')], max_length=15), blank=True, null=True, size=None),
        ),
        migrations.DeleteModel(
            name='MangaCategory',
        ),
        migrations.DeleteModel(
            name='MangaPerson',
        ),
        migrations.DeleteModel(
            name='MangaPoster',
        ),
        migrations.AddField(
            model_name='mangavolume',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga_api.Manga', verbose_name='Manga'),
        ),
        migrations.AddField(
            model_name='mangaimage',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga_api.MangaVolume', verbose_name='Volume'),
        ),
        migrations.AddField(
            model_name='manga',
            name='artists',
            field=models.ManyToManyField(blank=True, to='manga_api.MangaArtist', verbose_name='Artists'),
        ),
    ]
