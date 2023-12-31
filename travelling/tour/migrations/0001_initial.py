# Generated by Django 4.2.6 on 2023-10-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
