# Generated by Django 4.1.7 on 2023-07-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_removedstudent_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='admission_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
