from datetime import date
import uuid
import os

from PyPDF2 import PdfReader

from django.db import models

from datetime import timedelta

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.conf import settings
from django.db.models.signals import post_save


# from dicebear import Avatar


# def save(self, *args, **kwargs):
#     if not self.pk:
#         avatar = Avatar(sprites=['male'], id='user-{}'.format(self.pk))
#         self.profile_image.save(avatar.file_name, avatar.file, save=False)
#     super().save(*args, **kwargs)

# Create your models here.

GENDER = (
    ("male", "MALE"),
    ("female", "FEMAIL"),
)
FILE_TYPE = (("pdf", "PDF"), ("image", "IMAGE"))

# CALCULATE AGE:


def calculateAge(birthDate):
    today = date.today()
    age = (
        today.year
        - birthDate.year
        - ((today.month, today.day) < (birthDate.month, birthDate.day))
    )

    return age


def save_pdf_pages_attachment(sender, instance, created, **kwargs):

    if created:
        instance.save()


def create_health_status(sender, instance, **kwargs):
    try:
        health_status = ClientHealthStatus.objects.get(client=instance)
    except ClientHealthStatus.DoesNotExist:
        health_status = ClientHealthStatus.objects.create(client=instance,
                                                          heart_condition='Normal',
                                                          blood_sugar=80,
                                                          blood_pressure='120/80',
                                                          weight=70,
                                                          height=180,
                                                          smoking_status=False,
                                                          alcohol_consumption=False,
                                                          physical_activity='Moderate')
    return health_status


def profile_image_file_path(instance, filename):
    # Generate file path for new recipe image
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join("uploads/profile/", filename)


def pdf_page_count(link):
    # Load the pdf to the PdfFileReader object with default settings
    with open(link, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        num = len(pdf_reader.pages)
        print(f"The total number of pages in the pdf document is {num}")
    return num


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Creates and save a new user
        if not email:
            raise ValueError("Users must have an email address!")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        # Creates and save a new superuser
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(PermissionsMixin, AbstractBaseUser):
    # Custom user model supports email instead of username
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True,
                              upload_to=profile_image_file_path)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self) -> str:
        return self.email

    objects = UserManager()

    USERNAME_FIELD = "email"


class Address(models.Model):
    address_line1 = models.CharField(max_length=60)

    def __str__(self):
        return self.address_line1


class Client(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="clients")
    name = models.CharField(max_length=60)
    dob = models.DateField(null=True, blank=True)
    date_bonding = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    address = models.ForeignKey(
        "Address", on_delete=models.SET_NULL, null=True, blank=True
    )
    phone = models.CharField(max_length=60, null=True, blank=True)
    email = models.EmailField(max_length=60)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    image = models.ImageField(null=True, blank=True,
                              upload_to=profile_image_file_path)
    # image = models.ImageField(
    #     upload_to=product_image_file_path,
    #     default='uploads/product/4edc7b2c-0f96-4fb6-a8bc-22a61e47cd6f.png')

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk is None:
            self.age = calculateAge(self.dob)

        # if not self.pk:
        #     avatar = Avatar(sprites=[f'{self.gender}'],
        #                     id='client-{}'.format(self.pk))
        #     self.image.save(avatar.file_name, avatar.file, save=False)

        if self.pk is None:
            if self.gender == "male":
                self.image = "uploads/05e9ff3c-ee03-439b-8bc3-ad38b56a4859.png"
            else:
                self.image = "uploads/4edc7b2c-0f96-4fb6-a8bc-22a61e47cd6f.png"
        print(self.image)
        super(Client, self).save(*args, **kwargs)


class Attachment(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    client = models.ForeignKey(
        "Client", on_delete=models.CASCADE, related_name="attachments"
    )
    filename = models.CharField(max_length=120)
    file = models.FileField(upload_to="upload_files")
    page_count = models.PositiveIntegerField(null=True, blank=True)
    file_type = models.CharField(
        max_length=15, choices=FILE_TYPE, null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def __unicode__(self):
    #     return self.file.url

    def __str__(self):
        return self.file.url

    def save(self, *args, **kwargs):
        if self.pk is not None and self.file_type == "pdf":
            pdf = f"{settings.BASE_DIR}{self.file.url}"
            self.page_count = pdf_page_count(pdf)
        else:
            self.page_count = 1
        super(Attachment, self).save(*args, **kwargs)


post_save.connect(save_pdf_pages_attachment, Attachment)


class Treatment(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="treatments"
    )
    client = models.ForeignKey(
        "Client", on_delete=models.CASCADE, related_name="treatments"
    )
    appointment = models.ForeignKey(
        "Appointment", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="treatments"
    )
    note = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.client.name} - {self.note}'


class Appointment(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    client = models.ForeignKey(
        "Client", on_delete=models.CASCADE, related_name="appointments"
    )
    description = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField()
    date_to = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date",)

    def save(self, *args, **kwargs):
        if self.date_to is None:
            self.date_to = self.date + timedelta(hours=1)
        # if self.treatment is None:
        #     self.treatment = self.client.name

        super(Appointment, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.client.name} - {self.date}"


# class Note(models.Model):
#     user = models.ForeignKey(
#         "User", on_delete=models.SET_NULL, blank=True, null=True)
#     text = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.text


class Prescription(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="prescriptions")
    client = models.ForeignKey(
        "Client", on_delete=models.CASCADE, related_name="prescriptions"
    )
    appointment = models.ForeignKey(
        "Appointment", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="prescriptions"
    )
    medication = models.ForeignKey(
        "Medication", on_delete=models.CASCADE, related_name="prescriptions"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.client.name} - {self.medication}'


class Medication(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.SET_NULL, blank=True, null=True)
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=20)
    duration = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.medicine_name}'


class ClinicalExamination(models.Model):

    CHOICES = (
        ('class1', 'CLASS I'),
        ('class2', 'CLASS II'),
        ('class3', 'CLASS III'),
        ('normal', 'NORMAL'),
        ('acute', 'ACUTE'),
        ('obtuse', 'OBTUCE'),
        ('deep', 'DEEP'),
        ('competent', 'COMPETENT'),
        ('incompetent', 'INCOMPETENT'),
        ('partially_competent', 'PARTIALLY_COMPETENT'),
        ('dolichocephalic', 'DOLICHOCEPHALIC'),
        ('mesocephalic', 'MESOCEPHALIC'),
        ('brachycephalic', 'BRACHYCEPHALIC'),
        ('coincidence', 'COINIDENCE'),
        ('deviated_to_left', 'DEVIATED TO LEFT'),
        ('deviated_to_right', 'DEVIATED TO RIGHT'),
        ('good', 'GOOD'),
        ('fair', 'FAIR'),
        ('bad', 'BAD'),
        ('max', 'MAX'),
        ('mand', 'MAND')
    )

    user = models.ForeignKey(
        "User", on_delete=models.SET_NULL, blank=True, null=True)
    client = models.OneToOneField(
        'Client', on_delete=models.CASCADE, unique=True, related_name='examinations')
    skeletal_class = models.CharField(
        max_length=200, choices=CHOICES, default="class1")
    nasolabial_angle = models.CharField(
        max_length=200, choices=CHOICES, default='normal')
    nasolabial_sulcus = models.CharField(
        max_length=200, choices=CHOICES, default='normal')
    overjet = models.CharField(max_length=60, default='Diskjet')
    oral_hygiene = models.CharField(
        max_length=200, choices=CHOICES, default='good')
    lip_competency = models.CharField(
        max_length=200, choices=CHOICES, default='competent')
    face_form = models.CharField(
        max_length=200, choices=CHOICES, default='dolichocephalic')
    habit = models.CharField(max_length=60, default='Naughty')
    treated_arch = models.CharField(
        max_length=200, choices=CHOICES, default='max')
    molar_class_left = models.CharField(
        max_length=200, choices=CHOICES, default='class1')
    molar_class_right = models.CharField(
        max_length=200, choices=CHOICES, default='class1')
    tongue_size = models.CharField(max_length=60, default='Long')
    bracket_system = models.CharField(
        max_length=200, choices=CHOICES, default='class1')
    midline_upper = models.CharField(
        max_length=200, choices=CHOICES, default='coincidence')
    midline_lower = models.CharField(
        max_length=200, choices=CHOICES, default='coincidence')
    slot = models.CharField(max_length=60, default='normal')
    extraction_upper = models.CharField(
        max_length=200, choices=CHOICES, default='class1')
    extraction_lower = models.CharField(
        max_length=200, choices=CHOICES, default='class1')
    anchorage_upper = models.CharField(
        max_length=200, choices=CHOICES, default='class1')
    treatment_plan = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.client.name} - {self.created}'


class ClientHealthStatus(models.Model):
    client = models.OneToOneField(
        'Client', on_delete=models.CASCADE, related_name='health_status')
    heart_condition = models.CharField(max_length=100)
    blood_sugar = models.IntegerField()
    blood_pressure = models.CharField(max_length=100)
    weight = models.FloatField()
    height = models.FloatField()
    smoking_status = models.BooleanField()
    alcohol_consumption = models.BooleanField()
    physical_activity = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'Health Status of [{self.client.name}]'


post_save.connect(create_health_status, Client)


# FIX THIS BEFORE PROCEEDING:


# class MedicalHistory(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     condition = models.CharField(max_length=100)
#     treatment = models.CharField(max_length=100)
#     diagnosis_date = models.DateField()


# class DentalHistory(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     treatment = models.CharField(max_length=100)
#     tooth = models.CharField(max_length=100)
#     treatment_date = models.DateField()


# class FaceDetails(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     face_image = models.ImageField()
#     face_shape = models.CharField(max_length=20)
#     face_features = models.CharField(max_length=100)
#     face_details_date = models.DateField()

# class Prescription(models.Model):
#     user = models.ForeignKey('User', on_delete=models.CASCADE)
#     client = models.ForeignKey(
#         'Client', on_delete=models.CASCADE, related_name='prescriptions')
#     title = models.CharField(max_length=90, default='Prescription')
#     # description = models.CharField(max_length=200)
#     description = models.TextField(blank=True, null=True)
#     files = models.ManyToManyField(
#         'Attachment', related_name='test_results', blank=True)
#     has_appointment = models.BooleanField(default=False)
#     appointment = models.ForeignKey(
#         'Appointment',
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True
#     )
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

# class Meta:
#     ordering = ('-created',)

# @property
# def upload_files(self):
#     return self.attachment_set()

# def save(self, *args, **kwargs):
#     if self.appointment is not None:
#         self.has_appointment = True
#     super(Prescription, self).save(*args, **kwargs)

# def __str__(self):
#     return f'{self.client.name} - {self.created}'


"""
Here is a list of some common medicines that a dentist may use, along with the
types of medicine:
    1. Anesthetics: used to numb the area before a dental procedure.
    Examples include lidocaine and mepivacaine.
    2. Antibiotics: used to prevent or treat infection.
    Examples include amoxicillin, metronidazole, and clindamycin.
    3. Pain relievers: used to alleviate pain and discomfort following a
    dental procedure.
    Examples include ibuprofen and acetaminophen.
    4. Anti-inflammatory: used to reduce inflammation and swelling.
    Examples include ibuprofen, aspirin, and naproxen.
    5. Antiseptics: used to clean and disinfect the area before a dental
    procedure.
    Examples include hydrogen peroxide and chlorhexidine.
    6. Antihistamines: used to reduce allergic reactions. Examples include
    diphenhydramine (Benadryl) and loratadine (Claritin).
    7. Vasoconstrictors: used to decrease blood flow to the area being treated.
    Examples include epinephrine and phenylephrine.
    8. Fluoride: used to strengthen tooth enamel and prevent cavities.
    Examples include fluoride toothpaste and fluoride varnish.
    9. Bone grafting materials: used to replace missing bone in the jaw in
    preparation for dental implants.
    Examples include hydroxyapatite and beta-tricalcium phosphate.
    10. Sedatives: used to relax the patient during a dental procedure.
    Examples include nitrous oxide (laughing gas) and oral sedation with
    medications such as diazepam (Valium).

"""
