# Generated by Django 4.1 on 2023-01-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Term', models.PositiveIntegerField()),
                ('NoEmp', models.PositiveIntegerField()),
                ('GrAppv', models.PositiveIntegerField()),
                ('CreateJob', models.PositiveIntegerField()),
                ('Retainedjob', models.PositiveIntegerField()),
                ('FranchiseCode', models.PositiveIntegerField()),
            ],
        ),
    ]
