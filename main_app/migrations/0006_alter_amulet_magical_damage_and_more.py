# Generated by Django 4.1 on 2022-08-31 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_amulet_critical_damage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amulet',
            name='magical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='amulet',
            name='physical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chest',
            name='magical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chest',
            name='physical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='helm',
            name='magical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='helm',
            name='physical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='leg',
            name='magical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='leg',
            name='physical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ring',
            name='magical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ring',
            name='physical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='shield',
            name='magical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='shield',
            name='physical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trinket',
            name='magical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trinket',
            name='physical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='magical_damage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='physical_damage',
            field=models.FloatField(),
        ),
    ]
