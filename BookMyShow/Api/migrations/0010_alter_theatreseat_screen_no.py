# Generated by Django 4.0.5 on 2022-08-30 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0009_theatreseat_col_theatreseat_row_theatreseat_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theatreseat',
            name='screen_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.screen'),
        ),
    ]
