# Generated by Django 4.1.7 on 2023-08-02 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_student_admission_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='admissionform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('Name', models.CharField(max_length=30)),
                ('Mobile', models.CharField(max_length=12)),
                ('Alternate_Mobile', models.CharField(max_length=12)),
                ('Tranier', models.CharField(choices=[('Mr.Srinivas', 'Mr.Srinivas'), ('Mr.Madhukar', 'Mr.Madhukar'), ('Mr.Manohar', 'Mr.Manohar'), ('Mr.Suresh', 'Mr.Suresh'), ('Mr.PVR', 'Mr.PVR'), ('O', 'Other')], max_length=20)),
                ('Mode_of_Traning', models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], max_length=10)),
                ('Batch_timings', models.CharField(max_length=5)),
                ('DateOfjoining', models.DateField()),
                ('Batch_Number', models.CharField(max_length=5)),
                ('Qulification', models.CharField(max_length=10)),
                ('Work_experience', models.CharField(max_length=10)),
                ('Experience_or_Fresher', models.CharField(max_length=10)),
                ('Backlogs', models.CharField(max_length=5)),
                ('Linked', models.CharField(max_length=50)),
                ('Instagram', models.CharField(max_length=30)),
                ('Image', models.ImageField(null=True, upload_to='images/')),
                ('course_interest', models.CharField(choices=[('EASIER', 'Because this is easier than other courses.'), ('INTEREST', 'I absorbed myself I am quite interested on this course.'), ('SUGGESTION', 'My friend suggestion or parents suggestion.'), ('DEMAND', 'This course have highest demand in market.')], max_length=20)),
                ('v_cube_reason', models.CharField(choices=[('TRAINERS', 'VCUBE have professional trainers and process is good'), ('TRENDING', 'VCUBE is trending institute'), ('FRIEND', 'My friend suggestion'), ('ASSISTANCE', 'Because of 100 % assistance')], max_length=20)),
                ('expectations', models.CharField(choices=[('PLACEMENTS', '100 % placements'), ('KNOWLEDGE', 'Best training and best knowledge on particular course'), ('GUIDANCE', 'Best guidance + placement assistance'), ('NONE', 'No expectations')], max_length=20)),
                ('weakness', models.CharField(choices=[('FEAR', 'Stage fear'), ('COMMUNICATION', 'Lack of communication'), ('KNOWLEDGE', 'Lack of subject knowledge'), ('ALL', 'All the above')], max_length=20)),
                ('test_importance', models.CharField(choices=[('YES', 'Yes, it is'), ('NO', 'No'), ('UNKNOWN', 'I don’t know')], max_length=20)),
                ('mock_value', models.CharField(choices=[('YES', 'Yes, it is'), ('NO', 'No'), ('UNKNOWN', 'I don’t know')], max_length=20)),
                ('hear_about_us', models.CharField(choices=[('SOCIAL', 'Social media'), ('FRIEND', 'Friends reference'), ('RANDOM', 'Randomly')], max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.courses')),
            ],
        ),
    ]