from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class MusicStudentUser(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        null=False,
        validators=[RegexValidator(regex=r"^@[a-zA-Z0-9]{3,30}$",
                                   message="Username must start with @ and contain only letters and numbers.")],
        error_messages={
            "unique": "A user with that username already exists.",
            "blank": "Username cannot be blank.",
            "null": "Username cannot be null.",
            "max_length": "Username cannot be more than 30 characters long.",
            "invalid": "Username must start with @ and can only contain letters and numbers."
        })
    first_name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        error_messages={
            "blank": "First name cannot be blank.",
            "null": "First name cannot be null.",
            "max_length": "First name cannot be more than 50 characters long."
        })
    last_name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        error_messages={
            "blank": "Last name cannot be blank.",
            "null": "Last name cannot be null.",
            "max_length": "Last name cannot be more than 50 characters long."
        })
    email = models.EmailField(
        max_length=254,
        blank=False,
        null=False,
        unique=True,
        validators=[RegexValidator(regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
                                   message="Email must be a valid email address, containing alphanumeric characters.")],
        error_messages={
            "blank": "Email cannot be blank.",
            "null": "Email cannot be null.",
            "unique": "A user with that email already exists.",
            "max_length": "Email cannot be more than 254 characters long.",
            "invalid": "Email must be a valid email address, containing alphanumeric characters."
        })
    bio = models.TextField(
        max_length=520,
        blank=True,
        validators=[RegexValidator(regex=r"^[a-zA-Z0-9!@#$%^&*()_+-=,./<>?;':\"\[\]{}|`~ ]{0,520}$")],
        error_messages={
            "max_length": "Bio cannot be more than 520 characters long.",
            "invalid": "Bio can only contain alphanumeric characters and the following special characters: !@#$%^&*()_+-=,./<>?;':\"[]{}|`~"
        })