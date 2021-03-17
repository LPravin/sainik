# Generated by Django 3.1.5 on 2021-03-14 04:42

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
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'EXSERVICEMEN'), (2, 'WELFARE_OFFICER'), (3, 'DIRECTOR'), (4, 'KSB'), (5, 'RSB'), (6, 'ADMIN')])),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Caste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caste_name', models.CharField(max_length=50)),
            ],
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
                ('corps_name', models.CharField(max_length=55)),
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
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExServiceMen',
            fields=[
                ('esm_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender_name', models.CharField(max_length=6)),
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
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='RankCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RecordOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_office_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='RegTypeReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('religion_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=9)),
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
                ('trade_group', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ZilaSainikBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zb_name', models.CharField(max_length=50)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.state')),
            ],
        ),
        migrations.CreateModel(
            name='WidowDetail',
            fields=[
                ('esm_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('family_pension', models.CharField(max_length=6)),
                ('widow_next_of_kin', models.CharField(max_length=100)),
                ('widow_next_of_kin_relation', models.CharField(max_length=30)),
                ('widow_expiry_date', models.DateField()),
                ('whether_spouse_has_esm', models.CharField(choices=[('', '---------'), ('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('spouse_esm_no', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.exservicemen')),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_name', models.CharField(max_length=45)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.service')),
                ('trade_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exservicemen.tradegroup')),
            ],
        ),
        migrations.CreateModel(
            name='SpouseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(verbose_name='Date Of Birth')),
                ('aadhaar_no', models.CharField(max_length=12)),
                ('voter_id_no', models.CharField(max_length=12, verbose_name='Voter ID Number')),
                ('pan_no', models.CharField(max_length=10, verbose_name='Permanent Account Number(PAN)')),
                ('csd_no', models.CharField(max_length=19, verbose_name='CSD Number')),
                ('echs_no', models.CharField(max_length=14, verbose_name='ECHS Number')),
                ('ident_mark_1', models.CharField(max_length=70, verbose_name='Identification Mark 1')),
                ('ident_mark_2', models.CharField(max_length=70, verbose_name='Identification Mark 2')),
                ('marital_status', models.CharField(choices=[('', '---------'), ('S', 'Single'), ('M', 'Married'), ('D', 'Divorced'), ('W', 'Widower')], default=None, max_length=1)),
                ('marriage_date', models.DateField()),
                ('spouse_relation', models.CharField(choices=[('', '---------'), ('W', 'Wife'), ('H', 'Husband')], default=None, max_length=1)),
                ('spouse_employment_status', models.CharField(choices=[('', '---------'), ('E', 'Employed'), ('U', 'UnEmployed')], default=None, max_length=1)),
                ('spouse_profession', models.CharField(max_length=50)),
                ('spouse_retirement_date', models.DateField()),
                ('next_of_kin', models.CharField(max_length=50)),
                ('nok_relation', models.CharField(max_length=15, verbose_name='Next Of Kin Relation')),
                ('ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('spouse_qualification', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.civilqualification')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_no', models.CharField(max_length=9)),
                ('reg_date', models.DateField()),
                ('enrollment_date', models.DateField()),
                ('world_war_2', models.CharField(choices=[('', '---------'), ('Y', 'Yes'), ('N', 'No')], default=None, max_length=1)),
                ('operations', models.CharField(blank=True, max_length=100)),
                ('decorations', models.CharField(blank=True, max_length=100)),
                ('corps', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.corp')),
                ('group', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.tradegroup')),
                ('rank', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.rank')),
                ('rank_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.rankcategory')),
                ('record_office', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.recordoffice')),
                ('ref', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.service')),
                ('trade', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.trade')),
                ('zila_board_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.zilasainikboard')),
            ],
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
            name='PresentAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.CharField(max_length=7)),
                ('house_name', models.CharField(max_length=30)),
                ('street_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=25)),
                ('pincode', models.CharField(max_length=6)),
                ('is_address_same', models.BooleanField()),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.district')),
                ('ref', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(verbose_name='Date Of Birth')),
                ('aadhaar_no', models.CharField(max_length=12)),
                ('voter_id_no', models.CharField(max_length=12, verbose_name='Voter ID Number')),
                ('pan_no', models.CharField(max_length=10, verbose_name='Permanent Account Number(PAN)')),
                ('csd_no', models.CharField(max_length=19, verbose_name='CSD Number')),
                ('echs_no', models.CharField(max_length=14, verbose_name='ECHS Number')),
                ('ident_mark_1', models.CharField(max_length=70, verbose_name='Identification Mark 1')),
                ('ident_mark_2', models.CharField(max_length=70, verbose_name='Identification Mark 2')),
                ('gender', models.CharField(choices=[('', '---------'), ('M', 'Male'), ('F', 'Female')], default=None, max_length=1)),
                ('mother', models.CharField(max_length=100)),
                ('father', models.CharField(max_length=100)),
                ('birth_place', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=12)),
                ('mobile', models.CharField(max_length=10)),
                ('expiry_date', models.DateField(blank=True)),
                ('birth_district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.district')),
                ('birth_state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.state')),
                ('caste', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.caste')),
                ('caste_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.castecategory')),
                ('ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('esm_no', models.CharField(max_length=10)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.district')),
                ('ref', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('discharge_reason', models.CharField(choices=[('', '---------'), ('O', 'On Completion of Engagement'), ('R', 'Retired'), ('M', 'Medical'), ('I', 'Injury'), ('D', 'Dismissed'), ('V', 'VRS'), ('E', 'Expired')], default=None, max_length=1)),
                ('discharge_book_no', models.CharField(max_length=8)),
                ('ppo_no', models.CharField(max_length=8)),
                ('pension_sanctioned', models.CharField(max_length=6)),
                ('present_pension', models.CharField(max_length=6)),
                ('disability_pension', models.CharField(max_length=6)),
                ('disability_percent', models.CharField(max_length=3)),
                ('character', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.character')),
                ('medical_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.medicalcategory')),
                ('ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='medicalcategory',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.service'),
        ),
        migrations.AddField(
            model_name='exservicemen',
            name='reg_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.regtypereference'),
        ),
        migrations.CreateModel(
            name='EmploymentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_passed', models.CharField(blank=True, max_length=40, null=True)),
                ('employment_status', models.CharField(choices=[('', '---------'), ('E', 'Employed'), ('U', 'Unemployed'), ('R', 'Retired')], max_length=1)),
                ('willing_for_job', models.CharField(choices=[('', '---------'), ('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Whether willing for Employment Registration?')),
                ('security_job', models.CharField(choices=[('', '---------'), ('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Whether willing for security job?')),
                ('firesafety_sec_qualification', models.CharField(max_length=50, verbose_name='Courses completed in relation with firefighting or security')),
                ('employer', models.CharField(max_length=50)),
                ('monthly_income', models.CharField(max_length=7)),
                ('civil_retirement_date', models.DateField()),
                ('civil_ppo_no', models.CharField(max_length=8, verbose_name='Civil PPO Number')),
                ('civil_qualification', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.civilqualification')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exservicemen.department')),
                ('ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
            name='DependentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=50, verbose_name='Name')),
                ('dep_relation', models.CharField(choices=[('', '---------'), ('W', 'Wife'), ('S', 'Son'), ('D', 'Daughter'), ('H', 'Husband'), ('F', 'Father'), ('M', 'Mother'), ('s', 'Sister'), ('B', 'Brother')], default=None, max_length=1, verbose_name='Dependent Relation')),
                ('dep_dob', models.DateField(verbose_name='Date of Birth')),
                ('aadhaar_no', models.CharField(max_length=12, verbose_name='Aadhaar Number')),
                ('dep_qualification', models.CharField(max_length=40, verbose_name='Dependent Qualification')),
                ('academic_year', models.CharField(max_length=4)),
                ('emp_status', models.CharField(choices=[('', '---------'), ('E', 'Employed'), ('U', 'UnEmployed')], max_length=1, verbose_name='Employment Status')),
                ('marital_status', models.CharField(choices=[('', '---------'), ('U', 'Unmarried'), ('M', 'Married')], default=None, max_length=1)),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApplyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('basic_reg_type', models.CharField(blank=True, choices=[('', '---------'), ('E', 'Ex-Servicemen'), ('W', 'Widow of already registered Ex-Servicemen'), ('TE', 'Transferred Exservicemen'), ('TW', 'Transferred Widow'), ('UW', 'Widow of Unregistered/Died in service Ex-Servicemen')], default=None, max_length=2, null=True)),
                ('esm_no', models.CharField(blank=True, max_length=10, null=True)),
                ('expiry_date', models.DateField(blank=True, default=None, null=True)),
                ('service_no', models.CharField(blank=True, max_length=9, null=True)),
                ('discharge_book', models.FileField(blank=True, null=True, upload_to='images/discharge book')),
                ('ppo_book', models.ImageField(blank=True, null=True, upload_to='images/ppo book')),
                ('residence_certificate', models.ImageField(blank=True, null=True, upload_to='images/residence certificate')),
                ('death_certificate', models.ImageField(blank=True, null=True, upload_to='images/death death_certificate')),
                ('corps', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.corp')),
                ('district', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.district')),
                ('esm_reg_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.regtypereference')),
                ('group', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.tradegroup')),
                ('rank', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.rank')),
                ('rank_category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.rankcategory')),
                ('record_office', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.recordoffice')),
                ('ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.service')),
                ('state', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.state')),
                ('trade', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exservicemen.trade')),
                ('zsb', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exservicemen.zilasainikboard')),
            ],
        ),
    ]
