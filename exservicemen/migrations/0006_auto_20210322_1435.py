# Generated by Django 3.1.5 on 2021-03-22 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exservicemen', '0005_auto_20210322_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicedetail',
            old_name='zila_board_id',
            new_name='zila_board',
        ),
    ]