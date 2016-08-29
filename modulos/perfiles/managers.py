# -*- coding: cp1252 -*-
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, UserManager

__author__ = 'Juan'


class UsuariosManager(BaseUserManager):
    def create_user(self, username=None, email=None, password=None, last_name=None, first_name=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = UserManager.normalize_email(email)
        user = self.model(username=username, email=email,
                          last_name=last_name, first_name=first_name,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, last_name, first_name, **extra_fields):
        u = self.create_user(username, email, password, last_name, first_name, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u