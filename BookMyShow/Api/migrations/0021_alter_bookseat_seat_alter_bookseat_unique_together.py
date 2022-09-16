# Generated by Django 4.0.5 on 2022-09-12 04:53

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0020_movieshow_tecket_price_alter_bookseat_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookseat',
            name='seat',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5'), ('A6', 'A6'), ('A7', 'A7'), ('A8', 'A8'), ('A9', 'A9'), ('A10', 'A10'), ('A11', 'A11'), ('A12', 'A12'), ('A13', 'A13'), ('A14', 'A14'), ('A15', 'A15'), ('A16', 'A16'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4'), ('B5', 'B5'), ('B6', 'B6'), ('B7', 'B7'), ('B8', 'B8'), ('B9', 'B9'), ('B10', 'B10'), ('B11', 'B11'), ('B12', 'B12'), ('B13', 'B13'), ('B14', 'B14'), ('B15', 'B15'), ('B16', 'B16'), ('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('C7', 'C7'), ('C8', 'C8'), ('C9', 'C9'), ('C10', 'C10'), ('C11', 'C11'), ('C12', 'C12'), ('C13', 'C13'), ('C14', 'C14'), ('C15', 'C15'), ('C16', 'C16'), ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4'), ('D5', 'D5'), ('D6', 'D6'), ('D7', 'D7'), ('D8', 'D8'), ('D9', 'D9'), ('D10', 'D10'), ('D11', 'D11'), ('D12', 'D12'), ('D13', 'D13'), ('D14', 'D14'), ('D15', 'D15'), ('D16', 'D16'), ('E1', 'E1'), ('E2', 'E2'), ('E3', 'E3'), ('E4', 'E4'), ('E5', 'E5'), ('E6', 'E6'), ('E7', 'E7'), ('E8', 'E8'), ('E9', 'E9'), ('E10', 'E10'), ('E11', 'E11'), ('E12', 'E12'), ('E13', 'E13'), ('E14', 'E14'), ('E15', 'E15'), ('E16', 'E16'), ('F1', 'F1'), ('F2', 'F2'), ('F3', 'F3'), ('F4', 'F4'), ('F5', 'F5'), ('F6', 'F6'), ('F7', 'F7'), ('F8', 'F8'), ('F9', 'F9'), ('F10', 'F10'), ('F11', 'F11'), ('F12', 'F12'), ('F13', 'F13'), ('F14', 'F14'), ('F15', 'F15'), ('F16', 'F16'), ('G1', 'G1'), ('G2', 'G2'), ('G3', 'G3'), ('G4', 'G4'), ('G5', 'G5'), ('G6', 'G6'), ('G7', 'G7'), ('G8', 'G8'), ('G9', 'G9'), ('G10', 'G10'), ('G11', 'G11'), ('G12', 'G12'), ('G13', 'G13'), ('G14', 'G14'), ('G15', 'G15'), ('G16', 'G16'), ('H1', 'H1'), ('H2', 'H2'), ('H3', 'H3'), ('H4', 'H4'), ('H5', 'H5'), ('H6', 'H6'), ('H7', 'H7'), ('H8', 'H8'), ('H9', 'H9'), ('H10', 'H10'), ('H11', 'H11'), ('H12', 'H12'), ('H13', 'H13'), ('H14', 'H14'), ('H15', 'H15'), ('H16', 'H16'), ('I1', 'I1'), ('I2', 'I2'), ('I3', 'I3'), ('I4', 'I4'), ('I5', 'I5'), ('I6', 'I6'), ('I7', 'I7'), ('I8', 'I8'), ('I9', 'I9'), ('I10', 'I10'), ('I11', 'I11'), ('I12', 'I12'), ('I13', 'I13'), ('I14', 'I14'), ('I15', 'I15'), ('I16', 'I16'), ('J1', 'J1'), ('J2', 'J2'), ('J3', 'J3'), ('J4', 'J4'), ('J5', 'J5'), ('J6', 'J6'), ('J7', 'J7'), ('J8', 'J8'), ('J9', 'J9'), ('J10', 'J10'), ('J11', 'J11'), ('J12', 'J12'), ('J13', 'J13'), ('J14', 'J14'), ('J15', 'J15'), ('J16', 'J16')], max_length=3, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='bookseat',
            unique_together={('seat', 'show_id')},
        ),
    ]
