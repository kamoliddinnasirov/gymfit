# Generated by Django 4.1.3 on 2022-11-23 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weeks',
            options={'ordering': ('id',), 'verbose_name': 'week', 'verbose_name_plural': 'weeks'},
        ),
    ]
