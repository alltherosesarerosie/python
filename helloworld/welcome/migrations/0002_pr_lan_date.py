# Generated by Django 4.2.6 on 2023-10-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pr_lan',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
