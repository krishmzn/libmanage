# Generated by Django 5.0.3 on 2024-03-19 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksMgmtModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('ISBN', models.CharField(max_length=255)),
                ('availability', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]