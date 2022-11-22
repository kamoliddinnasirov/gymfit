# Generated by Django 4.1.3 on 2022-11-22 05:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_gallerylibrary_remove_gallery_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CourseBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('courses_title', models.CharField(blank=True, max_length=20, null=True, verbose_name='courses title')),
                ('courses_banner', models.ImageField(blank=True, null=True, upload_to='courses_banner/%Y/%m/%d/', verbose_name='courses banner')),
            ],
            options={
                'verbose_name': 'course banner',
                'verbose_name_plural': 'courses banner',
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=50, verbose_name='full_name')),
                ('is_active', models.BooleanField(default=False, verbose_name='is_active')),
            ],
            options={
                'verbose_name': 'mentor',
                'verbose_name_plural': 'mentors',
            },
        ),
        migrations.CreateModel(
            name='OurTrainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='full name')),
                ('achievement', models.CharField(max_length=100, verbose_name='achievement')),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('linkedin', models.URLField()),
                ('image', models.ImageField(default='some_value', upload_to='trainer_photo/%Y/%m/%d/', verbose_name='image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pages.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Our trainer',
                'verbose_name_plural': 'Our trainer',
            },
        ),
        migrations.CreateModel(
            name='PopularCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('from_time', models.DateTimeField(verbose_name='from time')),
                ('to_time', models.DateTimeField(verbose_name='to time')),
                ('main_banner', models.ImageField(upload_to='popular_course/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pages.category', verbose_name='course')),
            ],
            options={
                'verbose_name': 'popular course',
                'verbose_name_plural': 'popular courses',
            },
        ),
        migrations.CreateModel(
            name='PopularCourseGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='some_value', upload_to='PopularCourseGallery/')),
                ('is_active', models.BooleanField(default=False, verbose_name='is_active')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pages.popularcourse', verbose_name='gallery')),
            ],
            options={
                'verbose_name': 'gallery',
                'verbose_name_plural': 'gallery',
            },
        ),
        migrations.CreateModel(
            name='TrainerBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trainer_title', models.CharField(blank=True, max_length=20, null=True, verbose_name='trainer title')),
                ('trainer_banner', models.ImageField(blank=True, null=True, upload_to='trainer_banner/%Y/%m/%d/', verbose_name='trainer banner')),
            ],
            options={
                'verbose_name': 'trainer banner',
                'verbose_name_plural': 'trainer banners',
            },
        ),
        migrations.CreateModel(
            name='Weeks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name': 'week',
                'verbose_name_plural': 'weeks',
            },
        ),
        migrations.DeleteModel(
            name='GalleryLibrary',
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='some_value', upload_to='about_gallery/%Y/%m/%d/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='populartrainer',
            name='started',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(4)], verbose_name='started'),
        ),
        migrations.AddField(
            model_name='popularcourse',
            name='weeks',
            field=models.ManyToManyField(to='pages.weeks', verbose_name='weeks'),
        ),
        migrations.AddField(
            model_name='mentor',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pages.popularcourse', verbose_name='name'),
        ),
    ]
