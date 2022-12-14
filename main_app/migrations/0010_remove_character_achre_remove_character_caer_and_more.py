# Generated by Django 4.1 on 2022-09-12 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_character_achre_alter_character_caer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='achre',
        ),
        migrations.RemoveField(
            model_name='character',
            name='caer',
        ),
        migrations.AddField(
            model_name='character',
            name='achreon',
            field=models.CharField(choices=[(0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15), (8, 16), (9, 17), (10, 18)], default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='character',
            name='caeren',
            field=models.CharField(choices=[(0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15), (8, 16), (9, 17), (10, 18)], default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='character',
            name='constitution',
            field=models.CharField(choices=[(0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15), (8, 16), (9, 17), (10, 18)], default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='character',
            name='dexterity',
            field=models.CharField(choices=[(0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15), (8, 16), (9, 17), (10, 18)], default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='character',
            name='strength',
            field=models.CharField(choices=[(0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15), (8, 16), (9, 17), (10, 18)], default=0, max_length=2),
        ),
    ]
