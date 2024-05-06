# Generated by Django 5.0.4 on 2024-04-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('course', models.CharField(max_length=100)),
                ('dateofbirth', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
