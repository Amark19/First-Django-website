# Generated by Django 3.0.7 on 2020-06-30 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amarsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='description',
            new_name='desc',
        ),
    ]
