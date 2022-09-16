# Generated by Django 4.0.5 on 2022-09-12 03:55

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0018_alter_bookseat_book_seat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookseat',
            name='book_seat',
        ),
        migrations.AddField(
            model_name='bookseat',
            name='seat',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5'), ('A6', 'A6'), ('A7', 'A7'), ('A8', 'A8'), ('A9', 'A9'), ('A10', 'A10'), ('A11', 'A11'), ('A12', 'A12'), ('A13', 'A13'), ('A14', 'A14'), ('A15', 'A15'), ('A16', 'A16'), ('A17', 'A17'), ('A18', 'A18'), ('A19', 'A19'), ('A20', 'A20'), ('A21', 'A21'), ('A22', 'A22'), ('A23', 'A23'), ('A24', 'A24'), ('A25', 'A25'), ('A26', 'A26'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4'), ('B5', 'B5'), ('B6', 'B6'), ('B7', 'B7'), ('B8', 'B8'), ('B9', 'B9'), ('B10', 'B10'), ('B11', 'B11'), ('B12', 'B12'), ('B13', 'B13'), ('B14', 'B14'), ('B15', 'B15'), ('B16', 'B16'), ('B17', 'B17'), ('B18', 'B18'), ('B19', 'B19'), ('B20', 'B20'), ('B21', 'B21'), ('B22', 'B22'), ('B23', 'B23'), ('B24', 'B24'), ('B25', 'B25'), ('B26', 'B26'), ('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('C7', 'C7'), ('C8', 'C8'), ('C9', 'C9'), ('C10', 'C10'), ('C11', 'C11'), ('C12', 'C12'), ('C13', 'C13'), ('C14', 'C14'), ('C15', 'C15'), ('C16', 'C16'), ('C17', 'C17'), ('C18', 'C18'), ('C19', 'C19'), ('C20', 'C20'), ('C21', 'C21'), ('C22', 'C22'), ('C23', 'C23'), ('C24', 'C24'), ('C25', 'C25'), ('C26', 'C26'), ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4'), ('D5', 'D5'), ('D6', 'D6'), ('D7', 'D7'), ('D8', 'D8'), ('D9', 'D9'), ('D10', 'D10'), ('D11', 'D11'), ('D12', 'D12'), ('D13', 'D13'), ('D14', 'D14'), ('D15', 'D15'), ('D16', 'D16'), ('D17', 'D17'), ('D18', 'D18'), ('D19', 'D19'), ('D20', 'D20'), ('D21', 'D21'), ('D22', 'D22'), ('D23', 'D23'), ('D24', 'D24'), ('D25', 'D25'), ('D26', 'D26'), ('E1', 'E1'), ('E2', 'E2'), ('E3', 'E3'), ('E4', 'E4'), ('E5', 'E5'), ('E6', 'E6'), ('E7', 'E7'), ('E8', 'E8'), ('E9', 'E9'), ('E10', 'E10'), ('E11', 'E11'), ('E12', 'E12'), ('E13', 'E13'), ('E14', 'E14'), ('E15', 'E15'), ('E16', 'E16'), ('E17', 'E17'), ('E18', 'E18'), ('E19', 'E19'), ('E20', 'E20'), ('E21', 'E21'), ('E22', 'E22'), ('E23', 'E23'), ('E24', 'E24'), ('E25', 'E25'), ('E26', 'E26'), ('F1', 'F1'), ('F2', 'F2'), ('F3', 'F3'), ('F4', 'F4'), ('F5', 'F5'), ('F6', 'F6'), ('F7', 'F7'), ('F8', 'F8'), ('F9', 'F9'), ('F10', 'F10'), ('F11', 'F11'), ('F12', 'F12'), ('F13', 'F13'), ('F14', 'F14'), ('F15', 'F15'), ('F16', 'F16'), ('F17', 'F17'), ('F18', 'F18'), ('F19', 'F19'), ('F20', 'F20'), ('F21', 'F21'), ('F22', 'F22'), ('F23', 'F23'), ('F24', 'F24'), ('F25', 'F25'), ('F26', 'F26'), ('G1', 'G1'), ('G2', 'G2'), ('G3', 'G3'), ('G4', 'G4'), ('G5', 'G5'), ('G6', 'G6'), ('G7', 'G7'), ('G8', 'G8'), ('G9', 'G9'), ('G10', 'G10'), ('G11', 'G11'), ('G12', 'G12'), ('G13', 'G13'), ('G14', 'G14'), ('G15', 'G15'), ('G16', 'G16'), ('G17', 'G17'), ('G18', 'G18'), ('G19', 'G19'), ('G20', 'G20'), ('G21', 'G21'), ('G22', 'G22'), ('G23', 'G23'), ('G24', 'G24'), ('G25', 'G25'), ('G26', 'G26'), ('H1', 'H1'), ('H2', 'H2'), ('H3', 'H3'), ('H4', 'H4'), ('H5', 'H5'), ('H6', 'H6'), ('H7', 'H7'), ('H8', 'H8'), ('H9', 'H9'), ('H10', 'H10'), ('H11', 'H11'), ('H12', 'H12'), ('H13', 'H13'), ('H14', 'H14'), ('H15', 'H15'), ('H16', 'H16'), ('H17', 'H17'), ('H18', 'H18'), ('H19', 'H19'), ('H20', 'H20'), ('H21', 'H21'), ('H22', 'H22'), ('H23', 'H23'), ('H24', 'H24'), ('H25', 'H25'), ('H26', 'H26'), ('I1', 'I1'), ('I2', 'I2'), ('I3', 'I3'), ('I4', 'I4'), ('I5', 'I5'), ('I6', 'I6'), ('I7', 'I7'), ('I8', 'I8'), ('I9', 'I9'), ('I10', 'I10'), ('I11', 'I11'), ('I12', 'I12'), ('I13', 'I13'), ('I14', 'I14'), ('I15', 'I15'), ('I16', 'I16'), ('I17', 'I17'), ('I18', 'I18'), ('I19', 'I19'), ('I20', 'I20'), ('I21', 'I21'), ('I22', 'I22'), ('I23', 'I23'), ('I24', 'I24'), ('I25', 'I25'), ('I26', 'I26'), ('J1', 'J1'), ('J2', 'J2'), ('J3', 'J3'), ('J4', 'J4'), ('J5', 'J5'), ('J6', 'J6'), ('J7', 'J7'), ('J8', 'J8'), ('J9', 'J9'), ('J10', 'J10'), ('J11', 'J11'), ('J12', 'J12'), ('J13', 'J13'), ('J14', 'J14'), ('J15', 'J15'), ('J16', 'J16'), ('J17', 'J17'), ('J18', 'J18'), ('J19', 'J19'), ('J20', 'J20'), ('J21', 'J21'), ('J22', 'J22'), ('J23', 'J23'), ('J24', 'J24'), ('J25', 'J25'), ('J26', 'J26'), ('K1', 'K1'), ('K2', 'K2'), ('K3', 'K3'), ('K4', 'K4'), ('K5', 'K5'), ('K6', 'K6'), ('K7', 'K7'), ('K8', 'K8'), ('K9', 'K9'), ('K10', 'K10'), ('K11', 'K11'), ('K12', 'K12'), ('K13', 'K13'), ('K14', 'K14'), ('K15', 'K15'), ('K16', 'K16'), ('K17', 'K17'), ('K18', 'K18'), ('K19', 'K19'), ('K20', 'K20'), ('K21', 'K21'), ('K22', 'K22'), ('K23', 'K23'), ('K24', 'K24'), ('K25', 'K25'), ('K26', 'K26'), ('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3'), ('L4', 'L4'), ('L5', 'L5'), ('L6', 'L6'), ('L7', 'L7'), ('L8', 'L8'), ('L9', 'L9'), ('L10', 'L10'), ('L11', 'L11'), ('L12', 'L12'), ('L13', 'L13'), ('L14', 'L14'), ('L15', 'L15'), ('L16', 'L16'), ('L17', 'L17'), ('L18', 'L18'), ('L19', 'L19'), ('L20', 'L20'), ('L21', 'L21'), ('L22', 'L22'), ('L23', 'L23'), ('L24', 'L24'), ('L25', 'L25'), ('L26', 'L26'), ('M1', 'M1'), ('M2', 'M2'), ('M3', 'M3'), ('M4', 'M4'), ('M5', 'M5'), ('M6', 'M6'), ('M7', 'M7'), ('M8', 'M8'), ('M9', 'M9'), ('M10', 'M10'), ('M11', 'M11'), ('M12', 'M12'), ('M13', 'M13'), ('M14', 'M14'), ('M15', 'M15'), ('M16', 'M16'), ('M17', 'M17'), ('M18', 'M18'), ('M19', 'M19'), ('M20', 'M20'), ('M21', 'M21'), ('M22', 'M22'), ('M23', 'M23'), ('M24', 'M24'), ('M25', 'M25'), ('M26', 'M26'), ('N1', 'N1'), ('N2', 'N2'), ('N3', 'N3'), ('N4', 'N4'), ('N5', 'N5'), ('N6', 'N6'), ('N7', 'N7'), ('N8', 'N8'), ('N9', 'N9'), ('N10', 'N10'), ('N11', 'N11'), ('N12', 'N12'), ('N13', 'N13'), ('N14', 'N14'), ('N15', 'N15'), ('N16', 'N16'), ('N17', 'N17'), ('N18', 'N18'), ('N19', 'N19'), ('N20', 'N20'), ('N21', 'N21'), ('N22', 'N22'), ('N23', 'N23'), ('N24', 'N24'), ('N25', 'N25'), ('N26', 'N26'), ('O1', 'O1'), ('O2', 'O2'), ('O3', 'O3'), ('O4', 'O4'), ('O5', 'O5'), ('O6', 'O6'), ('O7', 'O7'), ('O8', 'O8'), ('O9', 'O9'), ('O10', 'O10'), ('O11', 'O11'), ('O12', 'O12'), ('O13', 'O13'), ('O14', 'O14'), ('O15', 'O15'), ('O16', 'O16'), ('O17', 'O17'), ('O18', 'O18'), ('O19', 'O19'), ('O20', 'O20'), ('O21', 'O21'), ('O22', 'O22'), ('O23', 'O23'), ('O24', 'O24'), ('O25', 'O25'), ('O26', 'O26'), ('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3'), ('P4', 'P4'), ('P5', 'P5'), ('P6', 'P6'), ('P7', 'P7'), ('P8', 'P8'), ('P9', 'P9'), ('P10', 'P10'), ('P11', 'P11'), ('P12', 'P12'), ('P13', 'P13'), ('P14', 'P14'), ('P15', 'P15'), ('P16', 'P16'), ('P17', 'P17'), ('P18', 'P18'), ('P19', 'P19'), ('P20', 'P20'), ('P21', 'P21'), ('P22', 'P22'), ('P23', 'P23'), ('P24', 'P24'), ('P25', 'P25'), ('P26', 'P26'), ('Q1', 'Q1'), ('Q2', 'Q2'), ('Q3', 'Q3'), ('Q4', 'Q4'), ('Q5', 'Q5'), ('Q6', 'Q6'), ('Q7', 'Q7'), ('Q8', 'Q8'), ('Q9', 'Q9'), ('Q10', 'Q10'), ('Q11', 'Q11'), ('Q12', 'Q12'), ('Q13', 'Q13'), ('Q14', 'Q14'), ('Q15', 'Q15'), ('Q16', 'Q16'), ('Q17', 'Q17'), ('Q18', 'Q18'), ('Q19', 'Q19'), ('Q20', 'Q20'), ('Q21', 'Q21'), ('Q22', 'Q22'), ('Q23', 'Q23'), ('Q24', 'Q24'), ('Q25', 'Q25'), ('Q26', 'Q26'), ('R1', 'R1'), ('R2', 'R2'), ('R3', 'R3'), ('R4', 'R4'), ('R5', 'R5'), ('R6', 'R6'), ('R7', 'R7'), ('R8', 'R8'), ('R9', 'R9'), ('R10', 'R10'), ('R11', 'R11'), ('R12', 'R12'), ('R13', 'R13'), ('R14', 'R14'), ('R15', 'R15'), ('R16', 'R16'), ('R17', 'R17'), ('R18', 'R18'), ('R19', 'R19'), ('R20', 'R20'), ('R21', 'R21'), ('R22', 'R22'), ('R23', 'R23'), ('R24', 'R24'), ('R25', 'R25'), ('R26', 'R26')], default='', max_length=3),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TheatreSeat',
        ),
    ]
