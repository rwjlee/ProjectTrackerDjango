# Generated by Django 2.0.4 on 2018-04-24 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(null=True, on_delete=True, related_name='has_tasks', to='user_info.User'),
        ),
    ]
