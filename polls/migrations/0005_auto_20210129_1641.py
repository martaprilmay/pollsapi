# Generated by Django 2.2.10 on 2021-01-29 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210129_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
    ]