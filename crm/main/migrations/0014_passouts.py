# Generated by Django 4.1.7 on 2023-06-02 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_courses_c_deatils_alter_courses_ckey'),
    ]

    operations = [
        migrations.CreateModel(
            name='passouts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('P_image', models.ImageField(null=True, upload_to='images/')),
                ('compnay', models.CharField(max_length=30)),
                ('package', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
            ],
        ),
    ]