# Generated by Django 4.1.3 on 2022-11-22 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_remove_popularcourse_main_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularcourse',
            name='from_time',
            field=models.DateField(verbose_name='from time'),
        ),
        migrations.AlterField(
            model_name='popularcourse',
            name='to_time',
            field=models.DateField(verbose_name='to time'),
        ),
    ]
