# Generated by Django 5.1.6 on 2025-02-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('eID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_passw', models.CharField(max_length=50)),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_doj', models.DateField(max_length=100)),
            ],
        ),
    ]
