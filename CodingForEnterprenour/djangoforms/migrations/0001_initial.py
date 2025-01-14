# Generated by Django 3.2.7 on 2022-07-27 14:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200, verbose_name='Post Title')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('views_count', models.IntegerField(default=0)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author_email', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
