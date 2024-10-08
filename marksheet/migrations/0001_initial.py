# Generated by Django 5.1 on 2024-08-31 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.CharField(max_length=20)),
                ('session', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Marksheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(null=True)),
                ('english_marks', models.IntegerField(null=True)),
                ('hindi_marks', models.IntegerField(null=True)),
                ('maths_marks', models.IntegerField(null=True)),
                ('science_marks', models.IntegerField(null=True)),
                ('socialstudy_marks', models.IntegerField(null=True)),
                ('session', models.CharField(choices=[('mid_year', 'Mid Year'), ('end_year', 'End Year')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('teachers', models.CharField(max_length=100)),
                ('books', models.CharField(max_length=100)),
            ],
        ),
    ]
