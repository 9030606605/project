# Generated by Django 4.1.7 on 2023-07-10 06:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_alter_interview_performance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='performance',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
