# Generated by Django 4.1.2 on 2022-10-22 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0008_alter_song_date_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='date_released',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]