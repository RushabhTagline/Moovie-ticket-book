# Generated by Django 4.0.5 on 2022-08-29 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_theatrescreenseat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estimation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_row', models.IntegerField(max_length=2)),
                ('total_col', models.IntegerField(max_length=2)),
            ],
        ),
    ]
