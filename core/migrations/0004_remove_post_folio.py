# Generated by Django 3.0.5 on 2020-04-15 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200415_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='folio',
        ),
    ]
