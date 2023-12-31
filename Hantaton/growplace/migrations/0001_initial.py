# Generated by Django 4.2.7 on 2023-11-25 10:53

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('datetimefield', models.DateTimeField()),
                ('loc', models.CharField(max_length=100)),
                ('imagefield', models.ImageField(blank=True, null=True, upload_to='images/events/')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='growplace.category')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.DateField()),
                ('tel_number', models.CharField(blank=True, max_length=20, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/user_photo/')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventOrganizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEvent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='growplace.event')),
                ('idOrganizer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=750)),
                ('idEvent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='growplace.event')),
            ],
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='growplace.category')),
                ('idEvent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='growplace.event')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('idCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='growplace.category')),
            ],
        ),
    ]
