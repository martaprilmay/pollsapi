# Generated by Django 2.2.10 on 2021-01-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20210130_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choices',
            field=models.ManyToManyField(blank=True, related_name='selected_choices', to='polls.Choice'),
        ),
    ]
