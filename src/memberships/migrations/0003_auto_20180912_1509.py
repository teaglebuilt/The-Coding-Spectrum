# Generated by Django 2.1 on 2018-09-12 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0002_auto_20180912_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='thread',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='first',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='second',
        ),
        migrations.DeleteModel(
            name='ChatMessage',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
