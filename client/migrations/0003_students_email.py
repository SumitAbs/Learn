# Generated by Django 5.1.4 on 2025-03-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='email',
            field=models.EmailField(blank=True, max_length=100, unique=True),
        ),
    ]
