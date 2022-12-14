# Generated by Django 4.1 on 2022-09-09 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='achre',
            field=models.CharField(choices=[(1, 8), (2, 9), (3, 10), (4, 11), (5, 12), (6, 13), (7, 14), (8, 15), (9, 16), (10, 17), (11, 18)], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='character',
            name='caer',
            field=models.CharField(choices=[(1, 8), (2, 9), (3, 10), (4, 11), (5, 12), (6, 13), (7, 14), (8, 15), (9, 16), (10, 17), (11, 18)], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='character',
            name='constitution',
            field=models.CharField(choices=[(1, 8), (2, 9), (3, 10), (4, 11), (5, 12), (6, 13), (7, 14), (8, 15), (9, 16), (10, 17), (11, 18)], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='character',
            name='dexterity',
            field=models.CharField(choices=[(1, 8), (2, 9), (3, 10), (4, 11), (5, 12), (6, 13), (7, 14), (8, 15), (9, 16), (10, 17), (11, 18)], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='character',
            name='strength',
            field=models.CharField(choices=[(1, 8), (2, 9), (3, 10), (4, 11), (5, 12), (6, 13), (7, 14), (8, 15), (9, 16), (10, 17), (11, 18)], default=1, max_length=2),
        ),
    ]
