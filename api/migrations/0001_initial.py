# Generated by Django 5.0.1 on 2024-01-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('email', models.EmailField(max_length=240)),
                ('phone', models.IntegerField()),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
