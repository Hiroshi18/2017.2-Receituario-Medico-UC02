from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    USERNAME_FIELD = ['email']
    REQUEIRED_FIELDS = ['name', 'date_of_birth', 'sex', 'email', 'sex']

    sex = models.CharField(blank=False, max_length=1)

    is_active = models.BooleanField(default=False)


class Patient(models.Model):

    patient = models.OneToOneField(User)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['name']
