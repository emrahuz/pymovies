# Generated by Django 2.2.7 on 2019-12-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20191221_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='fragman_link',
            field=models.CharField(default='', max_length=100, verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='movie',
            name='oyuncular',
            field=models.CharField(default='', max_length=200, verbose_name='Cast'),
        ),
        migrations.AddField(
            model_name='movie',
            name='yonetmen',
            field=models.CharField(default='', max_length=100, verbose_name='Director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb',
            field=models.FloatField(default='', max_length=50, verbose_name='Imdb'),
        ),
    ]
