# Generated by Django 2.2.6 on 2019-10-27 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planes', '0002_remove_planes_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='planes',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, to='planes.Valoracion'),
        ),
    ]
