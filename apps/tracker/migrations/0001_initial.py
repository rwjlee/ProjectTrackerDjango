# Generated by Django 2.0.4 on 2018-04-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=True, related_name='has_projects', to='user_info.User')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=True, related_name='has_tasks', to='tracker.Project')),
                ('user', models.ForeignKey(on_delete=True, related_name='has_tasks', to='user_info.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('project', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together={('user', 'name')},
        ),
    ]