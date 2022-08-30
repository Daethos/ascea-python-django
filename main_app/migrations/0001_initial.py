# Generated by Django 4.1 on 2022-08-28 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amulet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('physical_resistance', models.IntegerField()),
                ('magical_resistance', models.IntegerField()),
                ('physical_damage', models.IntegerField()),
                ('magical_damage', models.IntegerField()),
                ('critical_chance', models.IntegerField()),
                ('critical_damage', models.IntegerField()),
                ('dodge', models.IntegerField()),
                ('roll', models.IntegerField()),
                ('img_URL', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('type', models.CharField(max_length=48)),
                ('physical_resistance', models.IntegerField()),
                ('magical_resistance', models.IntegerField()),
                ('physical_damage', models.IntegerField()),
                ('magical_damage', models.IntegerField()),
                ('critical_chance', models.IntegerField()),
                ('critical_damage', models.IntegerField()),
                ('dodge', models.IntegerField()),
                ('roll', models.IntegerField()),
                ('img_URL', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Helm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('type', models.CharField(max_length=48)),
                ('physical_resistance', models.IntegerField()),
                ('magical_resistance', models.IntegerField()),
                ('physical_damage', models.IntegerField()),
                ('magical_damage', models.IntegerField()),
                ('critical_chance', models.IntegerField()),
                ('critical_damage', models.IntegerField()),
                ('dodge', models.IntegerField()),
                ('roll', models.IntegerField()),
                ('img_URL', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Legs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('type', models.CharField(max_length=48)),
                ('physical_resistance', models.IntegerField()),
                ('magical_resistance', models.IntegerField()),
                ('physical_damage', models.IntegerField()),
                ('magical_damage', models.IntegerField()),
                ('critical_chance', models.IntegerField()),
                ('critical_damage', models.IntegerField()),
                ('dodge', models.IntegerField()),
                ('roll', models.IntegerField()),
                ('img_URL', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('description', models.TextField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Ring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('physical_resistance', models.IntegerField()),
                ('magical_resistance', models.IntegerField()),
                ('physical_damage', models.IntegerField()),
                ('magical_damage', models.IntegerField()),
                ('critical_chance', models.IntegerField()),
                ('critical_damage', models.IntegerField()),
                ('dodge', models.IntegerField()),
                ('roll', models.IntegerField()),
                ('img_URL', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('type', models.CharField(max_length=48)),
                ('physical_resistance', models.IntegerField()),
                ('magical_resistance', models.IntegerField()),
                ('physical_damage', models.IntegerField()),
                ('magical_damage', models.IntegerField()),
                ('critical_chance', models.IntegerField()),
                ('critical_damage', models.IntegerField()),
                ('dodge', models.IntegerField()),
                ('roll', models.IntegerField()),
                ('img_URL', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trinket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('type', models.CharField(max_length=48)),
                ('physical_resistance', models.IntegerField()),
                ('magical_resistance', models.IntegerField()),
                ('physical_damage', models.IntegerField()),
                ('magical_damage', models.IntegerField()),
                ('critical_chance', models.IntegerField()),
                ('critical_damage', models.IntegerField()),
                ('dodge', models.IntegerField()),
                ('roll', models.IntegerField()),
                ('img_URL', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('type', models.CharField(max_length=48)),
                ('grip', models.CharField(max_length=48)),
                ('attack_type', models.CharField(max_length=48)),
                ('damage_type', models.CharField(max_length=48)),
                ('physical_damage', models.IntegerField()),
                ('magical_damage', models.IntegerField()),
                ('critical_chance', models.IntegerField()),
                ('critical_damage', models.IntegerField()),
                ('dodge', models.IntegerField()),
                ('roll', models.IntegerField()),
                ('img_URL', models.IntegerField()),
            ],
        ),
    ]
