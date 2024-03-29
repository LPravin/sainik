# Generated by Django 3.1.5 on 2021-06-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exservicemen', '0006_auto_20210624_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='dependentdetail',
            name='aadhaar_card',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='dependentdetail',
            name='echs_card',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='dependentdetail',
            name='pan_card',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='dependentdetail',
            name='voter_id',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='esmdocument',
            name='PPO',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='esmdocument',
            name='aadhaar_card',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='esmdocument',
            name='bank_pass_book',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='esmdocument',
            name='dc_book',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='esmdocument',
            name='echs_card',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='esmdocument',
            name='esm_death_certificate',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='esmdocument',
            name='group_photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='esmdocument',
            name='id_card',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='esmdocument',
            name='pan_card',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='esmdocument',
            name='self_photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='esmdocument',
            name='voter_id',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='spousedetail',
            name='aadhaar_card',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='spousedetail',
            name='echs_card',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='spousedetail',
            name='pan_card',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='spousedetail',
            name='voter_id',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
