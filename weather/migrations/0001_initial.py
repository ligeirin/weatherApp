# Generated by Django 5.0.6 on 2024-05-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLocale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
