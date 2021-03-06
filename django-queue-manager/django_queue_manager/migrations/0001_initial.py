# Generated by Django 2.0.4 on 2019-01-08 16:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DQMQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('queue_host', models.CharField(max_length=255)),
                ('queue_port', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)])),
                ('max_retries', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'DQMQueue',
                'verbose_name_plural': 'DQMQueues',
            },
        ),
        migrations.CreateModel(
            name='FailedTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_function_name', models.TextField()),
                ('task_args', models.TextField()),
                ('task_kwargs', models.TextField()),
                ('task_id', models.IntegerField()),
                ('exception', models.TextField()),
                ('failed_on', models.DateTimeField(auto_now_add=True)),
                ('pickled_task', models.BinaryField()),
                ('dqmqueue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_queue_manager.DQMQueue')),
            ],
            options={
                'verbose_name': 'Failed Task',
                'verbose_name_plural': 'Failed Tasks',
            },
        ),
        migrations.CreateModel(
            name='QueuedTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_function_name', models.TextField()),
                ('task_args', models.TextField()),
                ('task_kwargs', models.TextField()),
                ('pickled_task', models.BinaryField()),
                ('queued_on', models.DateTimeField(auto_now_add=True)),
                ('dqmqueue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_queue_manager.DQMQueue')),
            ],
            options={
                'verbose_name': 'Queued Task',
                'verbose_name_plural': 'Queued Tasks',
            },
        ),
        migrations.CreateModel(
            name='SuccessTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_function_name', models.TextField()),
                ('task_args', models.TextField()),
                ('task_kwargs', models.TextField()),
                ('task_id', models.IntegerField()),
                ('success_on', models.DateTimeField(auto_now_add=True)),
                ('pickled_task', models.BinaryField()),
                ('dqmqueue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_queue_manager.DQMQueue')),
            ],
            options={
                'verbose_name': 'Success Task',
                'verbose_name_plural': 'Success Tasks',
            },
        ),
    ]
