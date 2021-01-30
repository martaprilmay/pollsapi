# Generated by Django 2.2.10 on 2021-01-30 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20210130_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answered_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.AuthID'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='choices',
            field=models.ManyToManyField(blank=True, null=True, related_name='selected_choices', to='polls.Choice'),
        ),
    ]