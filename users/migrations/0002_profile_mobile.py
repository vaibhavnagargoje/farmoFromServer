# Generated by Django 5.0.3 on 2024-03-28 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(default=10, max_length=15),
            preserve_default=False,
        ),
    ]
