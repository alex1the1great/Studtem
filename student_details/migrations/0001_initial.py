# Generated by Django 3.0.6 on 2020-05-12 07:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('class_name', models.CharField(max_length=50)),
                ('dob', models.DateTimeField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('course_enroll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_details.Courses')),
            ],
        ),
    ]
