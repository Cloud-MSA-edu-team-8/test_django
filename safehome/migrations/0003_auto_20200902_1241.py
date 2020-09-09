# Generated by Django 3.1 on 2020-09-02 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('safehome', '0002_auto_20200902_0005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alcohol',
            old_name='region_code',
            new_name='region_info',
        ),
        migrations.RenameField(
            model_name='children',
            old_name='region_code',
            new_name='region_info',
        ),
        migrations.RenameField(
            model_name='crime',
            old_name='region_code',
            new_name='region_info',
        ),
        migrations.RenameField(
            model_name='fire_damage',
            old_name='region_code',
            new_name='region_info',
        ),
        migrations.RenameField(
            model_name='flood',
            old_name='region_code',
            new_name='region_info',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='region_code',
            new_name='region_info',
        ),
        migrations.RenameField(
            model_name='population',
            old_name='region_code',
            new_name='region_info',
        ),
        migrations.RenameField(
            model_name='total',
            old_name='region_code',
            new_name='region_info',
        ),
        migrations.RenameField(
            model_name='total_rate',
            old_name='region_code',
            new_name='region_info',
        ),
    ]