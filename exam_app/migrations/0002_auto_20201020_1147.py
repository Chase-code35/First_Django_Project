# Generated by Django 3.1.1 on 2020-10-20 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='alias',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]