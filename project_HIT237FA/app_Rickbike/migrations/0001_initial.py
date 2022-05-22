# Generated by Django 4.0.4 on 2022-05-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.CharField(max_length=12)),
                ('description', models.CharField(max_length=400)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]