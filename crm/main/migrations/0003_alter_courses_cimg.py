# Generated by Django 4.1.7 on 2023-05-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_courses_cdesc_courses_cimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='cimg',
            field=models.ImageField(null=True, upload_to='course_images/'),
        ),
    ]