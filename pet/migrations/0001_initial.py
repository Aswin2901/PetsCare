# Generated by Django 4.0 on 2023-02-14 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adno', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=15)),
                ('cls', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'studentdata',
            },
        ),
    ]
