# Generated by Django 4.1.7 on 2023-05-20 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_image_courses_image1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='image1',
            new_name='image',
        ),
    ]
