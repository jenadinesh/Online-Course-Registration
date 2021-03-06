# Generated by Django 2.2.12 on 2020-07-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=30, unique=True)),
                ('faculty', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('fee', models.FloatField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EnrollModel',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('cid', models.IntegerField()),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('contact', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
