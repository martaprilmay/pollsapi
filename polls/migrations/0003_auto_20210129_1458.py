# Generated by Django 2.2.10 on 2021-01-29 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0002_auto_20210129_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('poll', 'question', 'voted_by')},
        ),
    ]
