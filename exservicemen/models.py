from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 8)
        return self.create_user(email, password, **extra_fields)


class MyUser(AbstractBaseUser):
    ROLE_CHOICES = (
        (1, 'EXSERVICEMEN'),
        (2, 'WELFARE_OFFICER'),
        (3, 'DIRECTOR'),
        (4, 'RSB_HEAD'),
        (5, 'RSB_OFFICER'),
        (6, 'KSB_HEAD'),
        (7, 'KSB_OFFICER'),
        (8, 'SUPERUSER')
    )
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

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


class ESMType(models.Model):
    primary_key = models.SmallIntegerField(primary_key=True)
    esm_type = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.esm_type


class Service(models.Model):
    primary_key = models.SmallIntegerField(primary_key=True)
    service_name = models.CharField(max_length=9, unique=True)

    def __str__(self):
        return self.service_name


class TradeGroup(models.Model):
    trade_group = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return self.trade_group


class Trade(models.Model):
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    trade_group = models.ForeignKey(TradeGroup, on_delete=models.CASCADE)
    trade_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.trade_name


class RankCategory(models.Model):
    primary_key = models.SmallIntegerField(primary_key=True)
    rank_category = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.rank_category


class Rank(models.Model):
    rank_category = models.ForeignKey(RankCategory, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    rank = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return self.rank


class ServiceNoPrefix(models.Model):
    prefix = models.CharField(max_length=10, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    rank_category = models.ForeignKey(RankCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.prefix


class ServiceNoSuffix(models.Model):
    suffix = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.suffix


class RecordOffice(models.Model):
    record_office_name = models.CharField(max_length=60, unique=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.record_office_name


class Corp(models.Model):
    corps_name = models.CharField(max_length=55, unique=True)
    record_office = models.ForeignKey(RecordOffice, on_delete=models.CASCADE)

    def __str__(self):
        return self.corps_name


class DischargeReason(models.Model):
    reason = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.reason


class MedicalCategory(models.Model):
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    mc_name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.mc_name


class Character(models.Model):
    character = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.character


class Religion(models.Model):
    religion_name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.religion_name


class CasteCategory(models.Model):
    caste_category_name = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.caste_category_name


class Department(models.Model):
    dep_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.dep_name


class RajyaSainikBoard(models.Model):
    rsb_name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.rsb_name


class State(models.Model):
    state_name = models.CharField(max_length=45, unique=True)
    rsb = models.ForeignKey(RajyaSainikBoard, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.state_name


class ZilaSainikBoard(models.Model):
    zb_name = models.CharField(max_length=50, unique=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    code = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.zb_name


class District(models.Model):
    district_name = models.CharField(max_length=50, unique=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    zila_board = models.ForeignKey(ZilaSainikBoard, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.district_name


class CivilQualification(models.Model):
    primary_key = models.SmallIntegerField(primary_key=True)
    qualification = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.qualification


class Specialization(models.Model):
    specialization = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.specialization


class ExServiceMen(models.Model):
    statuses = (
        (1, 'ACTIVE'),
        (2, 'PENDING'),  # for exservicemen
        (3, 'EXPIRED'),
        (4, 'INCOMPLETE'),  # for welfare officer
        (5, 'UNDER QUERY'),
        (6, 'WAITING FOR VERIFICATION'),
        (7, 'SCHEDULED'),
        (8, 'TO BE RECOMMENDED BY WELFARE OFFICER'),
        (9, 'RECOMMENDED BY WELFARE OFFICER')
    )
    reg_categories = (
        (1, 'ESM'),
        (2, 'WIDOW'),
        (3, 'WIDOW IN SERVICE / UNREGISTERED')
    )
    esm_no = models.CharField(primary_key=True, max_length=10)
    reg_category = models.SmallIntegerField(choices=reg_categories)
    zila_board = models.ForeignKey(ZilaSainikBoard, on_delete=models.DO_NOTHING, default=None)
    status = models.PositiveSmallIntegerField(choices=statuses)

    def __str__(self):
        return self.esm_no


class LinkUserEsm(models.Model):
    ref_user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    ref_Esm = models.OneToOneField(ExServiceMen, on_delete=models.CASCADE)


class WidowDetail(models.Model):
    ref = models.OneToOneField(ExServiceMen, on_delete=models.CASCADE)
    spouse_esm_no = models.OneToOneField(ExServiceMen, on_delete=models.CASCADE, related_name='esm_reference')

    def __str__(self):
        return self.ref.esm_no


class ServiceDetail(models.Model):
    ref = models.OneToOneField(ExServiceMen, on_delete=models.CASCADE, related_name='servicedetail')
    name = models.CharField(max_length=100)
    dob = models.DateField(verbose_name="Date Of Birth")
    mobile = models.CharField(max_length=10, blank=True)
    reg_type = models.ForeignKey(ESMType, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    corps = models.ForeignKey(Corp, on_delete=models.DO_NOTHING, blank=True, null=True)
    record_office = models.ForeignKey(RecordOffice, on_delete=models.CASCADE)
    group = models.ForeignKey(TradeGroup, on_delete=models.CASCADE)
    trade = models.ForeignKey(Trade, on_delete=models.SET_NULL, blank=True, null=True)
    other_trade = models.CharField(max_length=50, blank=True, null=True)
    prefix = models.ForeignKey(ServiceNoPrefix, on_delete=models.CASCADE, blank=True, null=True)
    service_no = models.CharField(max_length=9)
    suffix = models.ForeignKey(ServiceNoSuffix, on_delete=models.CASCADE, blank=True, null=True)
    rank_category = models.ForeignKey(RankCategory, on_delete=models.SET_NULL, blank=True, null=True)
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING, default=None)
    other_rank = models.CharField(max_length=50, blank=True, null=True)
    reg_date = models.DateField()
    enrollment_date = models.DateField()
    world_war_2 = models.CharField(max_length=1, choices=YesNo, default=None)
    operations = models.CharField(max_length=100, blank=True, null=True)
    decorations = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ref.esm_no


class PensionDetail(models.Model):
    ref = models.OneToOneField(ExServiceMen, on_delete=models.CASCADE, related_name='pensiondetail')
    unit_last_served = models.CharField(max_length=50)
    discharge_date = models.DateField()
    discharge_reason = models.ForeignKey(DischargeReason, on_delete=models.CASCADE, default=None)
    medical_category = models.ForeignKey(MedicalCategory, on_delete=models.CASCADE, default=None)
    character = models.ForeignKey(Character, on_delete=models.DO_NOTHING, default=None)
    discharge_book_no = models.CharField(max_length=8)
    ppo_no = models.CharField(max_length=16, blank=True, verbose_name="PPO No")
    pensioner_status = models.CharField(max_length=1, choices=YesNo, default=None)
    pension_sanctioned = models.CharField(max_length=6, blank=True)
    present_pension = models.CharField(max_length=6, blank=True)
    whether_pwd = models.CharField(max_length=1, choices=YesNo, default=None)
    disability_pension = models.CharField(max_length=6, blank=True)
    disability_percent = models.CharField(max_length=3, blank=True)
    family_pension = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return self.ref.esm_no


class PersonalRef(models.Model):
    aadhaar_no = models.CharField(max_length=12, blank=True, null=True)
    voter_id_no = models.CharField(max_length=12, blank=True, null=True, verbose_name="Voter ID Number")
    pan_no = models.CharField(max_length=10, blank=True, null=True, verbose_name="Permanent Account Number(PAN)")
    csd_no = models.CharField(max_length=19, blank=True, null=True, verbose_name="CSD Number")
    echs_no = models.CharField(max_length=14, blank=True, null=True, verbose_name="ECHS Number")
    ident_mark_1 = models.CharField(max_length=70, blank=True, null=True, verbose_name="Identification Mark 1")
    ident_mark_2 = models.CharField(max_length=70, blank=True, null=True, verbose_name="Identification Mark 2")

    class Meta:
        abstract = True


class PersonalDetail(PersonalRef):
    Genders = [
        ('', '---------'),
        ('M', 'MALE'),
        ('F', 'FEMALE')
    ]

    ref = models.OneToOneField(ExServiceMen, on_delete=models.CASCADE, related_name='personaldetail')
    gender = models.CharField(max_length=1, choices=Genders, default=None)
    mother = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    religion = models.ForeignKey(Religion, on_delete=models.DO_NOTHING)
    caste_category = models.ForeignKey(CasteCategory, on_delete=models.DO_NOTHING, default=None)
    birth_place = models.CharField(max_length=50)
    birth_state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    birth_district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.ref.esm_no


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


class PermanentAddress(Address):
    ref = models.OneToOneField(ExServiceMen, on_delete=models.CASCADE, default=None, related_name='permanentaddress')
    telephone = models.CharField(max_length=12, blank=True, null=True)
    is_address_same = models.BooleanField(default=False)

    def __str__(self):
        return self.ref.esm_no


class PresentAddress(Address):
    ref = models.OneToOneField(ExServiceMen, on_delete=models.CASCADE, default=None, related_name='presentaddress')

    def __str__(self):
        return self.ref.esm_no


class EmploymentDetail(models.Model):
    EStates = [
        ('', '---------'),
        ('E', 'EMPLOYED'),
        ('U', 'UNEMPLOYED'),
        ('R', 'RETIRED')
    ]
    Sectors = [
        ('C', 'CENTRAL GOVERNMENT'),
        ('S', 'STATE GOVERNMENT'),
        ('P', 'PRIVATE'),
    ]
    ref = models.OneToOneField(ExServiceMen, on_delete=models.CASCADE, related_name='employmentdetail')
    civil_qualification = models.ForeignKey(CivilQualification, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, null=True, blank=True)
    test_passed = models.CharField(max_length=40, null=True, blank=True)
    employment_status = models.CharField(max_length=1, choices=EStates)
    willing_for_job = models.CharField(max_length=1, choices=YesNo, blank=True, null=True,
                                       verbose_name="Whether willing for Employment Registration?")
    security_job = models.CharField(max_length=1, choices=YesNo, verbose_name="Whether willing for security job?",
                                    blank=True, null=True)
    sector = models.CharField(max_length=1, choices=Sectors, blank=True, null=True)
    monthly_income = models.CharField(max_length=7, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True, blank=True)
    civil_retirement_date = models.DateField(null=True, blank=True)
    civil_ppo_no = models.CharField(max_length=8, verbose_name="Civil PPO Number", blank=True, null=True)

    def __str__(self):
        return self.ref.esm_no


class BasicDocument(models.Model):
    aadhaar_card = models.ImageField(null=True, blank=True)
    pan_card = models.ImageField(null=True, blank=True)
    echs_card = models.ImageField(null=True, blank=True)
    voter_id = models.ImageField(null=True, blank=True)

    class Meta:
        abstract = True


class SpouseDetail(PersonalRef, BasicDocument):
    MaritalStates = [
        ('', '---------'),
        ('S', 'SINGLE'),
        ('M', 'MARRIED'),
        ('D', 'DIVORCED'),
        ('W', 'WIDOWER')
    ]
    SpouseRelation = [
        ('', '---------'),
        ('W', 'WIFE'),
        ('H', 'HUSBAND')
    ]
    EmploymentStatus = [
        ('', '---------'),
        ('E', 'EMPLOYED'),
        ('U', 'UNEMPLOYED')
    ]
    ref = models.OneToOneField(ExServiceMen, on_delete=models.CASCADE, related_name='spousedetail')
    spouse_name = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(verbose_name="Date Of Birth", null=True, blank=True)
    marital_status = models.CharField(max_length=1, choices=MaritalStates, default=None)
    marriage_date = models.DateField(null=True, blank=True)
    spouse_relation = models.CharField(max_length=1, choices=SpouseRelation, default=None, null=True, blank=True)
    spouse_qualification = models.ForeignKey(CivilQualification, on_delete=models.DO_NOTHING, null=True, blank=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, blank=True, null=True)
    spouse_employment_status = models.CharField(max_length=1, choices=EmploymentStatus, default=None, blank=True,
                                                null=True)
    spouse_profession = models.CharField(max_length=50, blank=True, null=True)
    spouse_retirement_date = models.DateField(blank=True, null=True)
    next_of_kin = models.CharField(max_length=50)
    nok_relation = models.CharField(max_length=15, verbose_name="Next Of Kin Relation")
    widow_expiry_date = models.DateField(blank=True, null=True)
    spouse_next_of_kin = models.CharField(max_length=100)
    spouse_next_of_kin_relation = models.CharField(max_length=30)

    def __str__(self):
        return self.ref.esm_no


class DependentDetail(BasicDocument):
    MaritalState = [
        ('', '---------'),
        ('U', 'UNMARRIED'),
        ('M', 'MARRIED'),
    ]
    Dependents = [
        ('', '---------'),
        ('W', 'WIFE'),
        ('S', 'SON'),
        ('D', 'DAUGHTER'),
        ('H', 'HUSBAND'),
        ('F', 'FATHER'),
        ('M', 'MOTHER'),
    ]
    EmploymentStatus = [
        ('', '---------'),
        ('E', 'EMPLOYED'),
        ('U', 'UUEMPLOYED')
    ]
    ref = models.ForeignKey(ExServiceMen, on_delete=models.CASCADE, related_name='dependentdetail')
    dep_name = models.CharField(max_length=50, verbose_name="Name")
    dep_relation = models.CharField(max_length=1, choices=Dependents, default=None, verbose_name='Dependent Relation')
    dep_dob = models.DateField(verbose_name='Date of Birth')
    aadhaar_no = models.CharField(max_length=12, blank=True, verbose_name='Aadhaar Number')
    dep_qualification = models.ForeignKey(CivilQualification, on_delete=models.CASCADE,
                                          verbose_name='Dependent Qualification', blank=True, null=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, blank=True, null=True)
    academic_year = models.CharField(max_length=7)
    emp_status = models.CharField(max_length=1, choices=EmploymentStatus, verbose_name='Employment Status', null=True,
                                  blank=True)
    marital_status = models.CharField(max_length=1, choices=MaritalState, default=None)

    def __str__(self):
        return self.dep_name


class ESMDocument(BasicDocument):
    ref = models.OneToOneField(ExServiceMen, on_delete=models.CASCADE, related_name='esmdocument')
    dc_book = models.FileField(null=True)
    PPO = models.FileField(null=True)
    id_card = models.ImageField(null=True)
    bank_pass_book = models.ImageField(null=True)
    self_photo = models.ImageField(null=True)
    group_photo = models.ImageField(null=True)
    esm_death_certificate = models.ImageField(null=True)


class OfficerDetail(models.Model):
    name = models.CharField(max_length=100)
    ref = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class WelfareOfficer(OfficerDetail):
    zila_board = models.ForeignKey(ZilaSainikBoard, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Director(OfficerDetail):
    zila_board = models.ForeignKey(ZilaSainikBoard, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RSBOfficer(OfficerDetail):
    rsb = models.ForeignKey(RajyaSainikBoard, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RSBHead(OfficerDetail):
    rsb = models.ForeignKey(RajyaSainikBoard, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class KSBOfficer(OfficerDetail):
    pass

    def __str__(self):
        return self.name


class KSBHead(OfficerDetail):
    pass

    def __str__(self):
        return self.name


class TransferDetail(models.Model):
    ref = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    from_zsb = models.ForeignKey(ZilaSainikBoard, on_delete=models.CASCADE)
