# Generated by Django 5.1.3 on 2024-12-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=255)),
                ('ingredients', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('sort', models.CharField(max_length=255)),
                ('cuisine', models.CharField(max_length=255)),
            ],
        ),
    ]
