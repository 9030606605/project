# Generated by Django 4.1.7 on 2023-07-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_remove_interview_performance'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='performance',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
