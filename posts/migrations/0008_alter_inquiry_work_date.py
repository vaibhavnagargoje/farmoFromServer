# Generated by Django 5.0.3 on 2024-04-06 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_inquiry_work_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='work_date',
            field=models.DateField(),
        ),
    ]
