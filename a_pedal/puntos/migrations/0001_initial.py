# Generated by Django 2.2.6 on 2019-10-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Punto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('nombre', models.CharField(blank=True, max_length=25, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
