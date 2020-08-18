# Generated by Django 3.0.9 on 2020-08-18 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safehome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flood',
            fields=[
                ('id', models.IntegerField(default='', primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=30)),
                ('people', models.IntegerField(default=0)),
                ('houses', models.IntegerField(default=0)),
                ('buildings', models.IntegerField(default=0)),
                ('public', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('code', models.IntegerField(default='', primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
