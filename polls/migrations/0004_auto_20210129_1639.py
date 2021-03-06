# Generated by Django 2.2.10 on 2021-01-29 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_auto_20210129_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='pub_date',
            new_name='start_date',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='question',
            name='created_by',
        ),
        migrations.AddField(
            model_name='poll',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='poll',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.IntegerField(choices=[(1, 'Text'), (2, 'Select'), (3, 'Choice')], default=1),
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.ManyToManyField(related_name='selected_choices', to='polls.Choice')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
                ('selected_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('poll', 'question', 'selected_by')},
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(blank=True, max_length=128, null=True)),
                ('answered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
            ],
            options={
                'unique_together': {('poll', 'question', 'answered_by')},
            },
        ),
    ]
