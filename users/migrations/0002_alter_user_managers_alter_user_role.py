# Generated by Django 5.1.4 on 2024-12-20 15:10

import users.UserManager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.UserManager.CustomUserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'Doctor'), (3, 'Nurse'), (1, 'Admin')], null=True),
        ),
    ]