from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core import validators
from . import constants
from models import EmailField


class Name(models.CharField):
    validator_min_length = validators.MinLengthValidator(constants.
                                                         NAME_MIN_LENGTH,
                                                         message=constants.
                                                         NAME_SIZE)
    validator_max_length = validators.MaxLengthValidator(constants.
                                                         NAME_MAX_LENGHT,
                                                         message=constants.
                                                         NAME_SIZE)

    default_validators = [validator_min_length, validator_max_length]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = constants.NAME_MAX_LENGHT
        kwargs['default'] = ''
        kwargs['unique'] = True
        super(models.CharField, self).__init__(*args, **kwargs)


class DateOfBirth(models.DateField):
    validator_min_length = validators.MinLengthValidator(constants.
                                                         BIRTH_MIN_LENGTH,
                                                         message=constants.
                                                         BIRTH_SIZE)
    validator_max_length = validators.MaxLengthValidator(constants.
                                                         BIRTH_MAX_LENGHT,
                                                         message=constants.
                                                         BIRTH_SIZE)

    default_validators = [validator_min_length, validator_max_length]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = constants.BIRTH_MAX_LENGHT
        kwargs['default'] = ''
        kwargs['unique'] = True
        super(models.CharField, self).__init__(*args, **kwargs)


class Phone(models.CharField):
    validator_min_length = validators.MinLengthValidator(constants.
                                                         PHONE_MIN_LENGTH,
                                                         message=constants.
                                                         PHONE_SIZE)
    validator_max_length = validators.MaxLengthValidator(constants.
                                                         PHONE_MAX_LENGHT,
                                                         message=constants.
                                                         USERNAME_SIZE)

    default_validators = [validator_min_length, validator_max_length]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = constants.PHONE_MAX_LENGHT
        kwargs['default'] = ''
        kwargs['unique'] = True
        super(models.CharField, self).__init__(*args, **kwargs)


class Email(EmailField):
    validator = validators.EmailValidator(message=constants.EMAIL_FORMAT)

    default_validators = [validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = constants.EMAIL_FIELD_LENGTH
        kwargs['default'] = ''
        kwargs['unique'] = True
        super(EmailField, self).__init__(*args, **kwargs)


class Sex(models.CharField):
    validator_min_length = validators.MinLengthValidator(constants.
                                                         SEX_MIN_LENGTH,
                                                         message=constants.
                                                         SEX_SIZE)
    validator_max_length = validators.MaxLengthValidator(constants.
                                                         SEX_MAX_LENGHT,
                                                         message=constants.
                                                         SEX_SIZE)

    default_validators = [validator_min_length, validator_max_length]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = constants.SEX_MAX_LENGHT
        kwargs['default'] = ''
        kwargs['unique'] = True
        super(models.CharField, self).__init__(*args, **kwargs)


class IdDocument(models.CharField):
    pass


class User(AbstractBaseUser):
    USERNAME_FIELD = ['email']
    REQUEIRED_FIELDS = ['name', 'date_of_birth', 'sex', 'email', 'sex']

    name = Name()
    date_of_birth = DateOfBirth()
    phone = Phone()
    email = Email()
    sex = Sex()

    is_active = models.BooleanField(default=False)


class Patient(models.Model):

    patient = models.OneToOneField(User)
    id_document = IdDocument()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['name']
