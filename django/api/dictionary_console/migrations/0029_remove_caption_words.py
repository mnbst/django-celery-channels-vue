# Generated by Django 3.0.6 on 2020-05-25 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary_console', '0028_auto_20200523_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caption',
            name='words',
        ),
    ]