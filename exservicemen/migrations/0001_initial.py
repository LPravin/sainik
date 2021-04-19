# Generated by Django 3.1.5 on 2021-04-19 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email address')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'EXSERVICEMEN'), (2, 'WELFARE_OFFICER'), (3, 'DIRECTOR'), (4, 'RSB_HEAD'), (5, 'RSB_OFFICER'), (6, 'KSB_HEAD'), (7, 'KSB_OFFICER'), (8, 'SUPERUSER')], default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CasteCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caste_category_name', models.CharField(default=None, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CivilQualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Corp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corps_name', models.CharField(max_length=55, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DischargeReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ESMType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esm_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ExServiceMen',
            fields=[
                ('esm_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('mobile', models.CharField(blank=True, max_length=10)),
                ('reg_category', models.SmallIntegerField(choices=[(1, 'ESM'), (2, 'WIDOW'), (3, 'WIDOW IN SERVICE / UNREGISTERED')])),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'ACTIVE'), (2, 'PENDING'), (3, 'EXPIRED'), (4, 'INCOMPLETE'), (5, 'UNDER QUERY'), (6, 'WAITING FOR VERIFICATION'), (7, 'SCHEDULED'), (8, 'TO BE RECOMMENDED BY WELFARE OFFICER'), (9, 'RECOMMENDED BY WELFARE OFFICER')])),
            ],
        ),
        migrations.CreateModel(
            name='MedicalCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mc_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RajyaSainikBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rsb_name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=35, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RankCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_category', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecordOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_office_name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('religion_name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=9, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceNoSuffix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suffix', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=45)),
                ('rsb', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.rajyasainikboard')),
            ],
        ),
        migrations.CreateModel(
            name='TradeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_group', models.CharField(max_length=1, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZilaSainikBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zb_name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=2)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.state')),
            ],
        ),
        migrations.CreateModel(
            name='WidowDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.exservicemen')),
                ('spouse_esm_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='esm_reference', to='exservicemen.exservicemen')),
            ],
        ),
        migrations.CreateModel(
            name='WelfareOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('zila_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.zilasainikboard')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransferDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_zsb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.zilasainikboard')),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_name', models.CharField(max_length=45, unique=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.service')),
                ('trade_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.tradegroup')),
            ],
        ),
        migrations.CreateModel(
            name='SpouseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhaar_no', models.CharField(blank=True, max_length=12, null=True)),
                ('voter_id_no', models.CharField(blank=True, max_length=12, null=True, verbose_name='Voter ID Number')),
                ('pan_no', models.CharField(blank=True, max_length=10, null=True, verbose_name='Permanent Account Number(PAN)')),
                ('csd_no', models.CharField(blank=True, max_length=19, null=True, verbose_name='CSD Number')),
                ('echs_no', models.CharField(blank=True, max_length=14, null=True, verbose_name='ECHS Number')),
                ('ident_mark_1', models.CharField(blank=True, max_length=70, null=True, verbose_name='Identification Mark 1')),
                ('ident_mark_2', models.CharField(blank=True, max_length=70, null=True, verbose_name='Identification Mark 2')),
                ('spouse_name', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date Of Birth')),
                ('marital_status', models.CharField(choices=[('', '---------'), ('S', 'Single'), ('M', 'Married'), ('D', 'Divorced'), ('W', 'Widower')], default=None, max_length=1)),
                ('marriage_date', models.DateField(blank=True, null=True)),
                ('spouse_relation', models.CharField(blank=True, choices=[('', '---------'), ('W', 'Wife'), ('H', 'Husband')], default=None, max_length=1, null=True)),
                ('spouse_employment_status', models.CharField(blank=True, choices=[('', '---------'), ('E', 'Employed'), ('U', 'UnEmployed')], default=None, max_length=1, null=True)),
                ('spouse_profession', models.CharField(blank=True, max_length=50, null=True)),
                ('spouse_retirement_date', models.DateField(blank=True, null=True)),
                ('next_of_kin', models.CharField(max_length=50)),
                ('nok_relation', models.CharField(max_length=15, verbose_name='Next Of Kin Relation')),
                ('widow_expiry_date', models.DateField(blank=True, null=True)),
                ('spouse_next_of_kin', models.CharField(max_length=100)),
                ('spouse_next_of_kin_relation', models.CharField(max_length=30)),
                ('ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.exservicemen')),
                ('spouse_qualification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.civilqualification')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceNoPrefix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=10, null=True)),
                ('esm_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.esmtype')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(verbose_name='Date Of Birth')),
                ('service_no', models.CharField(max_length=9, unique=True)),
                ('reg_date', models.DateField()),
                ('enrollment_date', models.DateField()),
                ('world_war_2', models.CharField(choices=[('', '---------'), ('Y', 'Yes'), ('N', 'No')], default=None, max_length=1)),
                ('operations', models.CharField(blank=True, max_length=100, null=True)),
                ('decorations', models.CharField(blank=True, max_length=100, null=True)),
                ('corps', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.corp')),
                ('group', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.tradegroup')),
                ('prefix', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.servicenoprefix')),
                ('rank', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.rank')),
                ('rank_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.rankcategory')),
                ('record_office', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.recordoffice')),
                ('ref', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.exservicemen')),
                ('reg_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.esmtype')),
                ('service', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.service')),
                ('suffix', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.servicenosuffix')),
                ('trade', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.trade')),
            ],
        ),
        migrations.CreateModel(
            name='RSBOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rsb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.rajyasainikboard')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RSBHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rsb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.rajyasainikboard')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='recordoffice',
            name='service',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.service'),
        ),
        migrations.AddField(
            model_name='rank',
            name='rank_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.rankcategory'),
        ),
        migrations.AddField(
            model_name='rank',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.service'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_esm', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.exservicemen')),
                ('profile_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PresentAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.CharField(max_length=7)),
                ('house_name', models.CharField(max_length=30)),
                ('street_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=25)),
                ('pincode', models.CharField(max_length=6)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.district')),
                ('ref', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.exservicemen')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.state')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhaar_no', models.CharField(blank=True, max_length=12, null=True)),
                ('voter_id_no', models.CharField(blank=True, max_length=12, null=True, verbose_name='Voter ID Number')),
                ('pan_no', models.CharField(blank=True, max_length=10, null=True, verbose_name='Permanent Account Number(PAN)')),
                ('csd_no', models.CharField(blank=True, max_length=19, null=True, verbose_name='CSD Number')),
                ('echs_no', models.CharField(blank=True, max_length=14, null=True, verbose_name='ECHS Number')),
                ('ident_mark_1', models.CharField(blank=True, max_length=70, null=True, verbose_name='Identification Mark 1')),
                ('ident_mark_2', models.CharField(blank=True, max_length=70, null=True, verbose_name='Identification Mark 2')),
                ('gender', models.CharField(choices=[('', '---------'), ('M', 'Male'), ('F', 'Female')], default=None, max_length=1)),
                ('mother', models.CharField(max_length=100)),
                ('father', models.CharField(max_length=100)),
                ('birth_place', models.CharField(max_length=50)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('birth_district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.district')),
                ('birth_state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.state')),
                ('caste_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.castecategory')),
                ('ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.exservicemen')),
                ('religion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.religion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PermanentAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.CharField(max_length=7)),
                ('house_name', models.CharField(max_length=30)),
                ('street_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=25)),
                ('pincode', models.CharField(max_length=6)),
                ('telephone', models.CharField(blank=True, max_length=12, null=True)),
                ('is_address_same', models.BooleanField(default=False)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.district')),
                ('ref', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.exservicemen')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.state')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PensionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_last_served', models.CharField(max_length=50)),
                ('discharge_date', models.DateField()),
                ('discharge_book_no', models.CharField(max_length=8)),
                ('ppo_no', models.CharField(blank=True, max_length=8, verbose_name='PPO No')),
                ('pensioner_status', models.CharField(choices=[('', '---------'), ('Y', 'Yes'), ('N', 'No')], default=None, max_length=1)),
                ('pension_sanctioned', models.CharField(blank=True, max_length=6)),
                ('present_pension', models.CharField(blank=True, max_length=6)),
                ('whether_pwd', models.CharField(choices=[('', '---------'), ('Y', 'Yes'), ('N', 'No')], default=None, max_length=1)),
                ('disability_pension', models.CharField(blank=True, max_length=6)),
                ('disability_percent', models.CharField(blank=True, max_length=3)),
                ('family_pension', models.CharField(blank=True, max_length=6)),
                ('character', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.character')),
                ('discharge_reason', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.dischargereason')),
                ('medical_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.medicalcategory')),
                ('ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.exservicemen')),
            ],
        ),
        migrations.AddField(
            model_name='medicalcategory',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.service'),
        ),
        migrations.CreateModel(
            name='KSBOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KSBHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='exservicemen',
            name='zila_board',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.zilasainikboard'),
        ),
        migrations.CreateModel(
            name='EmploymentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_passed', models.CharField(blank=True, max_length=40, null=True)),
                ('employment_status', models.CharField(choices=[('', '---------'), ('E', 'Employed'), ('U', 'Unemployed'), ('R', 'Retired')], max_length=1)),
                ('willing_for_job', models.CharField(blank=True, choices=[('', '---------'), ('Y', 'Yes'), ('N', 'No')], max_length=1, null=True, verbose_name='Whether willing for Employment Registration?')),
                ('security_job', models.CharField(blank=True, choices=[('', '---------'), ('Y', 'Yes'), ('N', 'No')], max_length=1, null=True, verbose_name='Whether willing for security job?')),
                ('sector', models.CharField(blank=True, choices=[('C', 'Central Government'), ('S', 'State Government'), ('P', 'Private')], max_length=1, null=True)),
                ('monthly_income', models.CharField(blank=True, max_length=7, null=True)),
                ('civil_retirement_date', models.DateField(blank=True, null=True)),
                ('civil_ppo_no', models.CharField(blank=True, max_length=8, null=True, verbose_name='Civil PPO Number')),
                ('civil_qualification', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.civilqualification')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.department')),
                ('ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.exservicemen')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.state'),
        ),
        migrations.AddField(
            model_name='district',
            name='zila_board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.zilasainikboard'),
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('zila_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.zilasainikboard')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DependentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=50, verbose_name='Name')),
                ('dep_relation', models.CharField(choices=[('', '---------'), ('W', 'Wife'), ('S', 'Son'), ('D', 'Daughter'), ('H', 'Husband'), ('F', 'Father'), ('M', 'Mother')], default=None, max_length=1, verbose_name='Dependent Relation')),
                ('dep_dob', models.DateField(verbose_name='Date of Birth')),
                ('aadhaar_no', models.CharField(blank=True, max_length=12, verbose_name='Aadhaar Number')),
                ('dep_qualification', models.CharField(max_length=40, verbose_name='Dependent Qualification')),
                ('academic_year', models.CharField(max_length=4)),
                ('emp_status', models.CharField(blank=True, choices=[('', '---------'), ('E', 'Employed'), ('U', 'UnEmployed')], max_length=1, null=True, verbose_name='Employment Status')),
                ('marital_status', models.CharField(choices=[('', '---------'), ('U', 'Unmarried'), ('M', 'Married')], default=None, max_length=1)),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.exservicemen')),
            ],
        ),
        migrations.AddField(
            model_name='corp',
            name='record_office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.recordoffice'),
        ),
        migrations.CreateModel(
            name='BasicDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discharge_book', models.FileField(upload_to='documents')),
                ('ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
