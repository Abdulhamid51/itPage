# Generated by Django 3.2.5 on 2021-07-15 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, verbose_name='username')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='ismi')),
                ('surname', models.CharField(blank=True, max_length=150, verbose_name='familyasi')),
                ('git', models.CharField(blank=True, max_length=350, verbose_name='github link')),
                ('telegram', models.CharField(blank=True, max_length=350, verbose_name='telegram link')),
                ('phone', models.IntegerField(blank=True, verbose_name='tel no')),
                ('checked', models.BooleanField(blank=True, verbose_name='cheched')),
                ('follows', models.ManyToManyField(related_name='follows', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user_pro')),
            ],
        ),
    ]
