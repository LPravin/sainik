# Generated by Django 3.1.5 on 2021-03-22 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exservicemen', '0002_auto_20210320_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permanentaddress',
            name='esm_no',
        ),
        migrations.RemoveField(
            model_name='presentaddress',
            name='is_address_same',
        ),
        migrations.AddField(
            model_name='permanentaddress',
            name='is_address_same',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='permanentaddress',
            name='telephone',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
