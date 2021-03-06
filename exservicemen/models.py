from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


YesNo = [
    ('', '---------'),
    ('Y', 'Yes'),
    ('N', 'No')
]


class RegTypeReference(models.Model):
    reg_type = models.CharField(max_length=10)

    def __str__(self):
        return self.reg_type


class Service(models.Model):
    service_name = models.CharField(max_length=9)

    def __str__(self):
        return self.service_name


class TradeGroup(models.Model):
    trade_group = models.CharField(max_length=1)

    def __str__(self):
        return self.trade_group


class Trade(models.Model):
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    trade_group = models.ForeignKey(TradeGroup, on_delete=models.CASCADE)
    trade_name = models.CharField(max_length=45)

    def __str__(self):
        return self.trade_name


class RankCategory(models.Model):
    rank_category = models.CharField(max_length=10)

    def __str__(self):
        return self.rank_category


class Rank(models.Model):
    rank_category = models.ForeignKey(RankCategory, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    rank = models.CharField(max_length=35)

    def __str__(self):
        return self.rank


class Corp(models.Model):
    corps_name = models.CharField(max_length=55)

    def __str__(self):
        return self.corps_name


class RecordOffice(models.Model):
    record_office_name = models.CharField(max_length=60)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.record_office_name


class Gender(models.Model):
    gender_name = models.CharField(max_length=6)

    def __str__(self):
        return self.gender_name


class MedicalCategory(models.Model):
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    mc_name = models.CharField(max_length=10)

    def __str__(self):
        return self.mc_name


class Character(models.Model):
    character = models.CharField(max_length=20)

    def __str__(self):
        return self.character


class Religion(models.Model):
    religion_name = models.CharField(max_length=10)

    def __str__(self):
        return self.religion_name


class Caste(models.Model):
    caste_name = models.CharField(max_length=50)

    def __str__(self):
        return self.caste_name


class CasteCategory(models.Model):
    caste_category_name = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.caste_category_name


class Department(models.Model):
    dep_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dep_name


class RajyaSainikBoard(models.Model):
    rsb_name = models.CharField(max_length=50)

    def __str__(self):
        return self.rsb_name


class State(models.Model):
    state_name = models.CharField(max_length=45)
    rsb = models.ForeignKey(RajyaSainikBoard, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.state_name


class ZilaSainikBoard(models.Model):
    zb_name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.zb_name


class District(models.Model):
    district_name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    zila_board = models.ForeignKey(ZilaSainikBoard, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.district_name


class CivilQualification(models.Model):
    qualification = models.CharField(max_length=20)

    def __str__(self):
        return self.qualification


class ApplyDetail(models.Model):
    regtypes = [
        ('', '---------'),
        ('S', ' SELF'),
        ('W', 'WIDOW')
    ]
    ref = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    basic_reg_type = models.CharField(max_length=1, choices=regtypes, default=None)
    have_esm = models.CharField(max_length=1, choices=YesNo, default=None, blank=True, null=True)
    esm_no = models.CharField(max_length=10, blank=True, null=True)
    expiry_date = models.DateField(default=None, blank=True, null=True)
    esm_reg_type = models.ForeignKey(RegTypeReference, on_delete=models.CASCADE, default=None, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=None, blank=True, null=True)
    corps = models.ForeignKey(Corp, on_delete=models.CASCADE, default=None, blank=True, null=True)
    record_office = models.ForeignKey(RecordOffice, on_delete=models.CASCADE, default=None, blank=True, null=True)
    group = models.ForeignKey(TradeGroup, on_delete=models.CASCADE, default=None, blank=True, null=True)
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE, default=None, blank=True, null=True)
    rank_category = models.ForeignKey(RankCategory, on_delete=models.CASCADE, default=None, blank=True, null=True)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, default=None, blank=True, null=True)
    service_no = models.CharField(max_length=9, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=None, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, default=None, blank=True, null=True)
    discharge_book = models.ImageField(upload_to='images/discharge book', blank=True, null=True)
    ppo_book = models.ImageField(upload_to='images/ppo book', blank=True, null=True)
    residence_certificate = models.ImageField(upload_to='images/residence certificate', blank=True, null=True)
    death_certificate = models.ImageField(upload_to='images/death death_certificate', blank=True, null=True)


class ExServiceMen(models.Model):
    esm_no = models.CharField(primary_key=True, max_length=10)
    reg_type = models.ForeignKey(RegTypeReference, on_delete=models.DO_NOTHING, default=None)
    ref = models.OneToOneField(MyUser, on_delete=models.CASCADE)


class WidowDetail(models.Model):
    ref = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    esm_no = models.CharField(primary_key=True, max_length=10)
    family_pension = models.CharField(max_length=6)
    widow_next_of_kin = models.CharField(max_length=100)
    widow_next_of_kin_relation = models.CharField(max_length=30)
    widow_expiry_date = models.DateField()
    whether_spouse_has_esm = models.CharField(max_length=1, choices=YesNo)
    spouse_esm_no = models.OneToOneField(ExServiceMen, on_delete=models.CASCADE, blank=True)


class ServiceDetail(models.Model):
    ref = models.OneToOneField(MyUser, on_delete=models.CASCADE, default=None)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, default=None)
    corps = models.ForeignKey(Corp, on_delete=models.DO_NOTHING, default=None, blank=True)
    record_office = models.ForeignKey(RecordOffice, on_delete=models.CASCADE, default=None)
    group = models.ForeignKey(TradeGroup, on_delete=models.CASCADE, default=None)
    trade = models.ForeignKey(Trade, on_delete=models.DO_NOTHING, default=None)
    service_no = models.CharField(max_length=9)
    rank_category = models.ForeignKey(RankCategory, on_delete=models.DO_NOTHING, default=None)
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING, default=None)
    reg_date = models.DateField()
    enrollment_date = models.DateField()
    world_war_2 = models.CharField(max_length=1, choices=YesNo, default=None)
    operations = models.CharField(max_length=100, blank=True)
    decorations = models.CharField(max_length=100, blank=True)
    zila_board_id = models.ForeignKey(ZilaSainikBoard, on_delete=models.DO_NOTHING, default=None)


class PensionDetail(models.Model):
    DischargeReasons = [
        ('', '---------'),
        ('O', 'On Completion of Engagement'),
        ('R', 'Retired'),
        ('M', 'Medical'),
        ('I', 'Injury'),
        ('D', 'Dismissed'),
        ('V', 'VRS'),
        ('E', 'Expired')
    ]
    ref = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    unit_last_served = models.CharField(max_length=50)
    discharge_date = models.DateField()
    discharge_reason = models.CharField(max_length=1, choices=DischargeReasons, default=None)
    medical_category = models.ForeignKey(MedicalCategory, on_delete=models.CASCADE, default=None)
    character = models.ForeignKey(Character, on_delete=models.DO_NOTHING, default=None)
    discharge_book_no = models.CharField(max_length=8)
    ppo_no = models.CharField(max_length=8)


class PersonalRef(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(verbose_name="Date Of Birth")
    aadhaar_no = models.CharField(max_length=12)
    voter_id_no = models.CharField(max_length=12, verbose_name="Voter ID Number")
    pan_no = models.CharField(max_length=10, verbose_name="Permanent Account Number(PAN)")
    csd_no = models.CharField(max_length=19, verbose_name="CSD Number")
    echs_no = models.CharField(max_length=14, verbose_name="ECHS Number")
    ident_mark_1 = models.CharField(max_length=70, verbose_name="Identification Mark 1")
    ident_mark_2 = models.CharField(max_length=70, verbose_name="Identification Mark 2")

    class Meta:
        abstract = True


class PersonalDetail(PersonalRef):
    Genders = [
        ('', '---------'),
        ('M', 'Male'),
        ('F', 'Female')
    ]

    ref = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=Genders, default=None)
    mother = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    religion = models.ForeignKey(Religion, on_delete=models.DO_NOTHING)
    caste = models.ForeignKey(Caste, on_delete=models.DO_NOTHING)
    caste_category = models.ForeignKey(CasteCategory, on_delete=models.DO_NOTHING, default=None)
    birth_place = models.CharField(max_length=50)
    birth_state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    birth_district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    pension_sanctioned = models.CharField(max_length=6)
    present_pension = models.CharField(max_length=6)
    disability_pension = models.CharField(max_length=6)
    disability_percent = models.CharField(max_length=3)
    pension_account_no = models.CharField(max_length=20)
    telephone = models.CharField(max_length=12)
    mobile = models.CharField(max_length=10)
    expiry_date = models.DateField(blank=True)


class Address(models.Model):
    house_no = models.CharField(max_length=7)
    house_name = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    city = models.CharField(max_length=25)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    pincode = models.CharField(max_length=6)

    class Meta:
        abstract = True


class PresentAddress(Address):
    ref = models.OneToOneField(MyUser, on_delete=models.CASCADE, default=None)
    is_address_same = models.BooleanField()


class PermanentAddress(Address):
    ref = models.OneToOneField(MyUser, on_delete=models.CASCADE, default=None)
    esm_no = models.CharField(max_length=10)


class EmploymentDetail(models.Model):
    EStates = [
        ('', '---------'),
        ('E', 'Employed'),
        ('U', 'Unemployed'),
        ('R', 'Retired')
    ]
    ref = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    civil_qualification = models.ForeignKey(CivilQualification, on_delete=models.DO_NOTHING)
    test_passed = models.CharField(max_length=40)
    employment_status = models.CharField(max_length=1, choices=EStates)
    willing_for_job = models.CharField(max_length=1, choices=YesNo, verbose_name="Whether willing for job?")
    security_job = models.CharField(max_length=1, choices=YesNo, verbose_name="Whether willing for security job?")
    firesafety_sec_qualification = models.CharField(max_length=50, verbose_name= "Courses completed in relation with firefighting or security")
    employer = models.CharField(max_length=50)
    monthly_income = models.CharField(max_length=7)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    civil_retirement_date = models.DateField()
    civil_ppo_no = models.CharField(max_length=8)


class SpouseDetail(PersonalRef):
    MaritalStates = [
        ('', '---------'),
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widower')
    ]
    SpouseRelation = [
        ('', '---------'),
        ('W', 'Wife'),
        ('H', 'Husband')
    ]
    EmploymentStatus = [
        ('', '---------'),
        ('E', 'Employed'),
        ('U', 'UnEmployed')
    ]
    ref = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    marital_status = models.CharField(max_length=1, choices=MaritalStates, default=None)
    marriage_date = models.DateField()
    spouse_relation = models.CharField(max_length=1, choices=SpouseRelation, default=None)
    spouse_qualification = models.ForeignKey(CivilQualification, on_delete=models.DO_NOTHING)
    spouse_employment_status = models.CharField(max_length=1, choices=EmploymentStatus, default=None)
    spouse_profession = models.CharField(max_length=50)
    spouse_retirement_date = models.DateField()
    next_of_kin = models.CharField(max_length=50)
    nok_relation = models.CharField(max_length=15, verbose_name="Next Of Kin Relation")


class DependentDetail(models.Model):
    MaritalState = [
        ('', '---------'),
        ('U', 'Unmarried'),
        ('M', 'Married'),
    ]
    Dependents = [
        ('', '---------'),
        ('W', 'Wife'),
        ('S', 'Son'),
        ('D', 'Daughter'),
        ('H', 'Husband'),
        ('F', 'Father'),
        ('M', 'Mother'),
    ]
    EmploymentStatus = [
        ('', '---------'),
        ('E', 'Employed'),
        ('U', 'UnEmployed')
    ]
    ref = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    aadhaar_no = models.CharField(max_length=12)
    dep_name = models.CharField(max_length=50)
    dep_relation = models.CharField(max_length=1, choices=Dependents, default=None)
    dep_qualification = models.CharField(max_length=40)
    academic_year = models.CharField(max_length=4)
    emp_status = models.CharField(max_length=1, choices=EmploymentStatus)
    marital_status = models.CharField(max_length=1, choices=MaritalState, default=None)
