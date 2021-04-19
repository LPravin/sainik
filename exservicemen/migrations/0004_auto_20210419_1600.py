# Generated by Django 3.1.5 on 2021-04-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exservicemen', '0003_auto_20210419_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='character',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='civilqualification',
            name='qualification',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='dep_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='district_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='esmtype',
            name='esm_type',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='medicalcategory',
            name='mc_name',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='rajyasainikboard',
            name='code',
            field=models.CharField(max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='rajyasainikboard',
            name='rsb_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='specialization',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='state_name',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='zilasainikboard',
            name='code',
            field=models.CharField(max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='zilasainikboard',
            name='zb_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
