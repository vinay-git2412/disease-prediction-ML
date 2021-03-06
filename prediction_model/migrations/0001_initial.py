# Generated by Django 4.0.5 on 2022-07-01 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DesandPrec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField(max_length=300)),
                ('Precaution_1', models.TextField(max_length=300)),
                ('Precaution_2', models.TextField(max_length=300)),
                ('Precaution_3', models.TextField(max_length=300)),
                ('Precaution_4', models.TextField(max_length=300)),
                ('classification', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='diseasePrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symptom1', models.CharField(max_length=20)),
                ('Symptom2', models.CharField(max_length=20)),
                ('Symptom3', models.CharField(max_length=20)),
                ('Symptom4', models.CharField(max_length=20)),
                ('Symptom5', models.CharField(max_length=20)),
                ('Symptom6', models.CharField(max_length=20)),
                ('classification', models.CharField(max_length=20)),
            ],
        ),
    ]
