# Generated by Django 3.1.5 on 2021-04-14 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exservicemen', '0015_auto_20210414_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widowdetail',
            name='family_pension',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='widowdetail',
            name='widow_expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
