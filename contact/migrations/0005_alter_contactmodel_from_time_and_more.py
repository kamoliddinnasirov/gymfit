# Generated by Django 4.1.3 on 2022-11-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_contactsendmodel_sub_title_contactsendmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='from_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='to_time',
            field=models.TimeField(),
        ),
    ]
