# Generated by Django 3.2.14 on 2022-08-05 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='gallery/'),
        ),
    ]
