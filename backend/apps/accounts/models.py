from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator, RegexValidator, EmailValidator
# Create your models here.

class CustomUser(AbstractUser):
    THEMES_CHOICES = (
        ('light', 'Light'),
        ('dark', 'Dark'),
    )

    UNIT_CHOICES = (
        ('metric', 'Metric'),
        ('imperial', 'Imperial'),
    )

    # no needed list
    first_name = None
    last_name = None

    # username 
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[MinLengthValidator(3), MaxLengthValidator(50)]
    )

    # email
    email = models.EmailField(
        unique=True, db_index=True,
        validators=[
            MinLengthValidator(5), 
            MaxLengthValidator(254),
            EmailValidator(message='Invalid email format')
        ]
    )

    # phone number optional
    phone_number = models.CharField(
        max_length=15, 
        null=True, 
        blank=True, 
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Invalid phone number format')]
    )


    # Notes
    # Null= True means that the field can be left blank
    # Blank= True means that the field is not required
    unit = models.CharField(max_length=9, choices=UNIT_CHOICES, default='metric')
    theme = models.CharField(max_length=7, choices=THEMES_CHOICES, default='dark')
    
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(13), MaxValueValidator(120)],
        help_text="Age in years" # this help_text is for the admin panel
    ) 

    weight = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        null=True, 
        blank=True, 
        help_text="Weight in kg", # this help_text is for the admin panel
        validators=[MinValueValidator(0)]
    )

    height = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        null=True, 
        blank=True, 
        help_text="Height in cm", # this help_text is for the admin panel
        validators=[MinValueValidator(0)]
    )

    # this is a json field that will store the schedule of the user. 
    # no need to validate it since it will be validated in the frontend allowings users only to select days of the week
    schedule = models.JSONField(default=dict, blank=True, null=True)

    is_active = models.BooleanField(default=True) 

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.username

