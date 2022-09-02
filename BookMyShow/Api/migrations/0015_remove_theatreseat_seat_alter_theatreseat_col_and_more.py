# Generated by Django 4.0.5 on 2022-08-31 04:11

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0014_alter_theatreseat_seat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theatreseat',
            name='seat',
        ),
        migrations.AlterField(
            model_name='theatreseat',
            name='col',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='theatreseat',
            name='row',
            field=models.IntegerField(default=12),
        ),
        migrations.CreateModel(
            name='BookSeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('seat', multiselectfield.db.fields.MultiSelectField(max_length=3, unique=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('show_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.movieshow')),
            ],
        ),
    ]
