from django.db import models
from django.contrib.auth.models import User


YesNo = [
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


class Group(models.Model):
    group = models.CharField(max_length=1)

    def __str__(self):
        return self.group


class Trade(models.Model):
    service_id = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    group = models.CharField(max_length=1)
    trade_name = models.CharField(max_length=45)

    def __str__(self):
        return self.trade_name


class RankCategory(models.Model):
    rank_category = models.CharField(max_length=6)

    def __str__(self):
        return self.rank_category


class Rank(models.Model):
    rank_category = models.ForeignKey(RankCategory, on_delete=models.DO_NOTHING)
    service_id = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    rank = models.CharField(max_length=35)

    def __str__(self):
        return self.rank


class Corp(models.Model):
    corps_name = models.CharField(max_length=55)

    def __str__(self):
        return self.corps_name


class Gender(models.Model):
    gender_name = models.CharField(max_length=6)

    def __str__(self):
        return self.gender_name


class MedicalCategory(models.Model):
    service_id = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
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
    state_id = models.SmallIntegerField(primary_key=True)
    state_name = models.CharField(max_length=45)
    rsb_id = models.ForeignKey(RajyaSainikBoard, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.state_name


class ZilaSainikBoard(models.Model):
    zb_name = models.CharField(max_length=50)
    state_id = models.ForeignKey(State, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.zb_name


class District(models.Model):
    district_id = models.SmallIntegerField(primary_key=True)
    district_name = models.CharField(max_length=50)
    state_id = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    zb_id = models.ForeignKey(ZilaSainikBoard, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.district_name


class CivilQualification(models.Model):
    cq_id = models.SmallIntegerField(primary_key=True)
    q_name = models.CharField(max_length=20)

    def __str__(self):
        return self.q_name


class ExServiceMen(models.Model):
    esm_no = models.CharField(primary_key=True, max_length=10)
    reg_type = models.ForeignKey(RegTypeReference, on_delete=models.DO_NOTHING, default=None)


class WidowDetail(models.Model):
    ref = models.OneToOneField(ExServiceMen, related_name='widowesmnoref', on_delete=models.CASCADE)
    family_pension = models.CharField(max_length=6)
    widow_next_of_kin = models.CharField(max_length=100)
    widow_next_of_kin_relation = models.CharField(max_length=30)
    widow_expiry_date = models.DateField()
    spouse_esm_no = models.OneToOneField(ExServiceMen, related_name='widowspouseref',on_delete=models.CASCADE, blank=True)


class ServiceDetail(models.Model):
    DischargeReasons = [
        ('O', 'On Completion of Engagement'),
        ('R', 'Retired'),
        ('M', 'Medical'),
        ('I', 'Injury'),
        ('D', 'Dismissed'),
        ('V', 'VRS'),
        ('E', 'Expired')
    ]
    ref = models.OneToOneField(ExServiceMen, on_delete=models.CASCADE, default=None)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, default=None)
    corps = models.ForeignKey(Corp, on_delete=models.DO_NOTHING, default=None, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=None)
    trade = models.ForeignKey(Trade, on_delete=models.DO_NOTHING, default=None)
    service_no = models.CharField(max_length=9)
    rank_category = models.ForeignKey(RankCategory, on_delete=models.DO_NOTHING, default=None)
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING, default=None)
    unit_last_served = models.CharField(max_length=50)
    discharge_date = models.DateField()
    discharge_reason = models.CharField(max_length=1, choices=DischargeReasons, default=None)
    medical_category = models.ForeignKey(MedicalCategory, on_delete=models.CASCADE, default=None)
    character = models.ForeignKey(Character, on_delete=models.DO_NOTHING, default=None)
    discharge_book_no = models.CharField(max_length=8)
    ppo_no = models.CharField(max_length=8)
    reg_date = models.DateField()
    enrollment_date = models.DateField()
    world_war_2 = models.CharField(max_length=1, choices=YesNo, default=None)
    operations = models.CharField(max_length=100, blank=True)
    decorations = models.CharField(max_length=100, blank=True)
    zila_board_id = models.ForeignKey(ZilaSainikBoard, on_delete=models.DO_NOTHING, default=None)


class PersonalDetail(models.Model):
    Genders = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    ref = models.OneToOneField(ServiceDetail, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=Genders, default=None)
    dob = models.DateField()
    mother = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    religion = models.ForeignKey(Religion, on_delete=models.DO_NOTHING)
    caste = models.ForeignKey(Caste, on_delete=models.DO_NOTHING)
    caste_category = models.ForeignKey(CasteCategory, on_delete=models.DO_NOTHING, default=None)
    birth_place = models.CharField(max_length=50)
    birth_state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    birth_district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    aadhaar_no = models.CharField(max_length=12)
    voter_id_no = models.CharField(max_length=12)
    pan_no = models.CharField(max_length=10)
    csd_no = models.CharField(max_length=19)
    echs_no = models.CharField(max_length=14)
    ident_mark_1 = models.CharField(max_length=70)
    ident_mark_2 = models.CharField(max_length=70)
    esm_expiry_date = models.DateField(blank=True)
    pension_sanctioned = models.CharField(max_length=6)
    present_pension = models.CharField(max_length=6)
    disability_pension = models.CharField(max_length=6)
    disability_percent = models.CharField(max_length=3)
    pension_account_no = models.CharField(max_length=20)
    telephone = models.CharField(max_length=12)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=30)


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
    ref = models.OneToOneField(ServiceDetail, on_delete=models.CASCADE, default=None)
    is_address_same = models.BooleanField()


class PermanentAddress(Address):
    ref = models.OneToOneField(ServiceDetail, on_delete=models.CASCADE, default=None)
    esm_no = models.CharField(max_length=10)


class EmploymentDetail(models.Model):
    EStates = [
        ('E', 'Employed'),
        ('U', 'Unemployed'),
        ('R', 'Retired')
    ]
    ref = models.OneToOneField(ServiceDetail, on_delete=models.CASCADE)
    civil_qualification = models.ForeignKey(CivilQualification, on_delete=models.DO_NOTHING)
    test_passed = models.CharField(max_length=40)
    employment_status = models.CharField(max_length=1, choices=EStates)
    willing_for_job = models.CharField(max_length=1, choices=YesNo)
    security_job = models.CharField(max_length=1, choices=YesNo)
    firesafety_sec_qualification = models.CharField(max_length=50)
    employer = models.CharField(max_length=50)
    monthly_income = models.CharField(max_length=7)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    civil_retirement_date = models.DateField()
    civil_ppo_no = models.CharField(max_length=8)


class SpouseDetail(models.Model):
    MaritalStates = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widower')
    ]
    SpouseRelation = [
        ('W', 'Wife'),
        ('H', 'Husband')
    ]
    EmploymentStatus = [
        ('E', 'Employed'),
        ('U', 'UnEmployed')
    ]
    ref = models.OneToOneField(ServiceDetail, on_delete=models.CASCADE)
    marital_status = models.CharField(max_length=1, choices=MaritalStates, default=None)
    marriage_date = models.DateField()
    spouse_name = models.CharField(max_length=100)
    spouse_relation = models.CharField(max_length=1, choices=SpouseRelation, default=None)
    spouse_dob = models.DateField()
    spouse_ident_mark1 = models.CharField(max_length=40)
    spouse_ident_mark2 = models.CharField(max_length=40)
    spouse_qualification = models.ForeignKey(CivilQualification, on_delete=models.DO_NOTHING)
    spouse_employment_status = models.CharField(max_length=1, choices=EmploymentStatus, default=None)
    spouse_profession = models.CharField(max_length=50)
    spouse_retirement_date = models.DateField()
    spouse_aadhaar = models.CharField(max_length=12)
    spouse_voter_id = models.CharField(max_length=12)
    spouse_pan = models.CharField(max_length=10)
    spouse_csd = models.CharField(max_length=19)
    spouse_echs = models.CharField(max_length=14)
    next_of_kin = models.CharField(max_length=50)
    nok_relation = models.CharField(max_length=15)


class DependentDetail(models.Model):
    MaritalState = [
        ('U', 'Unmarried'),
        ('M', 'Married'),
    ]
    Dependents = [
        ('W', 'Wife'),
        ('S', 'Son'),
        ('D', 'Daughter'),
        ('H', 'Husband'),
        ('F', 'Father'),
        ('M', 'Mother'),
    ]
    ref = models.ForeignKey(ServiceDetail, on_delete=models.CASCADE)
    aadhaar_no = models.CharField(max_length=12)
    dep_name = models.CharField(max_length=50)
    dep_relation = models.CharField(max_length=1, choices=Dependents, default=None)
    dep_qualification = models.CharField(max_length=40)
    academic_year = models.CharField(max_length=4)
    emp_status = models.CharField(max_length=1, )
    marital_status = models.CharField(max_length=1, choices=MaritalState, default=None)