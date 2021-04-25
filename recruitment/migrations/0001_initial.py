# Generated by Django 2.2.4 on 2020-02-19 06:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('application_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.datetime(2020, 2, 19, 6, 17, 26, 775795, tzinfo=utc))),
                ('post', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=255)),
                ('department', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('category', models.CharField(choices=[('GEN', 'General'), ('SC', 'SC'), ('ST', 'ST'), ('OBC-CL', 'OBC Creamy Layer'), ('OBC-NCL', 'OBC Non Creamy Layer'), ('GEN-PWD', 'General Person with disabilties'), ('OBC-CL-PWD', 'OBC Creamy Layer Person with disabilites'), ('OBC-NCL-PWD', 'OBC Non Creamy Layer Person with disabilites'), ('SC-PWD', 'SC person with disabilites'), ('ST-PWD', 'ST person with disabilites')], max_length=25)),
                ('reservation', models.CharField(blank=True, choices=[('GEN', 'General'), ('SC', 'SC'), ('ST', 'ST'), ('OBC-NCL', 'OBC Non Creamy Layer'), ('PWD', 'General Person with disabilties'), ('SERVICE', 'Ex-Service Man'), ('GEN-ECO', 'General Category Economically Weaker Sections')], max_length=25, null=True)),
                ('current_address', models.TextField()),
                ('permanent_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teaching_and_research_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=200)),
                ('level', models.CharField(choices=[('UG', 'Undergraduate'), ('PG', 'Postgraduate')], max_length=2)),
                ('sole_instructor', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('developer_of_course', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('name_of_student', models.CharField(max_length=200)),
                ('year_of_completion', models.IntegerField()),
                ('name_of_institute', models.CharField(max_length=200)),
                ('guide', models.CharField(max_length=200)),
                ('organisation', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('co_investigators', models.CharField(max_length=200)),
                ('period', models.CharField(max_length=100)),
                ('name_of_body', models.CharField(max_length=150)),
                ('status_of_membership', models.CharField(max_length=150)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teaching_and_research_detail', to='recruitment.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Profession_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('from_year', models.IntegerField()),
                ('to_year', models.IntegerField()),
                ('role', models.CharField(max_length=250)),
                ('pay_scale', models.IntegerField()),
                ('emoluments', models.IntegerField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professional_details', to='recruitment.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Other_important_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awards_and_recognition', models.TextField()),
                ('any_other_relevant_information', models.TextField()),
                ('reference', models.TextField()),
                ('statement_of_objective', models.TextField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_details', to='recruitment.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publications', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('caste_certificate', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='recruitment.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Academic_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('area_of_qualification', models.CharField(max_length=200)),
                ('category_of_university', models.CharField(max_length=200)),
                ('institute', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('ResultAwaited', 'ResultAwaited'), ('FinalAwaited', 'FinalAwaited'), ('Ongoing', 'Ongoing')], max_length=200)),
                ('year_of_passing', models.IntegerField()),
                ('percentage', models.IntegerField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_detail', to='recruitment.Applicant')),
            ],
        ),
    ]
