# Generated by Django 4.1.3 on 2022-11-24 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_ourtrainer_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourtrainer',
            name='image',
        ),
    ]