# Generated by Django 4.1.3 on 2022-11-25 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='title')),
                ('services', models.CharField(max_length=50, verbose_name='services')),
                ('continue_package', models.CharField(max_length=50, verbose_name='continue package')),
                ('price', models.PositiveIntegerField()),
                ('check_close', models.BooleanField(help_text='(0)-close, (1)-check', verbose_name='check close')),
                ('popular', models.BooleanField(help_text='(check)-popular')),
            ],
            options={
                'verbose_name': 'package',
                'verbose_name_plural': 'packages',
            },
        ),
    ]
