# Generated by Django 3.2.4 on 2021-07-01 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_goals', '0002_auto_20210701_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='relevent',
            new_name='relevant',
        ),
    ]
