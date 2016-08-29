# -*- coding: cp1252 -*-
import django.utils
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.template.loader import render_to_string

from django.utils import timezone
import datetime

from dateutil.relativedelta import *
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from modulos.configurador.models import TipoUsuario

from modulos.perfiles.managers import UsuariosManager


from django.utils.translation import ugettext_lazy as _

from modulos.maestras.models import  Maestra


class Perfil(AbstractBaseUser, PermissionsMixin):
    objects = UsuariosManager()
    REQUIRED_FIELDS = ['email']
    creado = models.DateTimeField(auto_now_add=True) # fecha de creacion
    modificado = models.DateTimeField(auto_now=True)# las_modify ultima modificacion
    activo = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now, blank=True, null=True)
    username = models.CharField(max_length=255,null=False,blank=False,unique=True)
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False)
    first_name = models.CharField(_('first name'), max_length=256, blank=False, null=True)
    celular= models.CharField(  max_length=256, blank=False, null=True)
    last_name = models.CharField(_('last name'), max_length=256, blank=False, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    tipo=models.ForeignKey(TipoUsuario,null=True,blank=True)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin '
                                             'site.')
    is_active = models.BooleanField('active', default=True,
                                    help_text='Designates whether this user should be treated as '
                                              'active. Unselect this instead of deleting accounts.')




    @classmethod
    def GetFieldsSerializer(self):
        fields_tmp = self._meta.fields
        fields_tmp = map(lambda x: x.name, fields_tmp)
        return [x for x in fields_tmp if x not in []]

    @property
    def edad(self):
        # Get the current date
        if self.fecha_nacimiento:
            now = datetime.datetime.utcnow()
            now = now.date()
            # Get the difference between the current date and the birthday

            age = relativedelta(now, self.fecha_nacimiento)
            age = age.years
            if age>0:
                self.edad_real=age
                self.save()
            return age
        return 0

    class Meta:
        verbose_name = u"Usuario"
        verbose_name_plural = "Usuarios"
        #unique_together=('rol','grupo')
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    @property
    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def email_user(self,subject, message, DEFAULT_FROM_EMAIL):
        subject, from_email, to = subject, DEFAULT_FROM_EMAIL, self.email
        text_content = message
        html_content = message
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


    @property
    def activation_key(self):
        return self.id

    def send_activation_email(self, site):
        """
        Send an activation email to the user associated with this
        ``RegistrationProfile``.

        The activation email will make use of two templates:

        ``registration/activation_email_subject.txt``
            This template will be used for the subject line of the
            email. Because it is used as the subject line of an email,
            this template's output **must** be only a single line of
            text; output longer than one line will be forcibly joined
            into only a single line.

        ``registration/activation_email.txt``
            This template will be used for the body of the email.

        These templates will each receive the following context
        variables:

        ``activation_key``
            The activation key for the new account.

        ``expiration_days``
            The number of days remaining during which the account may
            be activated.

        ``site``
            An object representing the site on which the user
            registered; depending on whether ``django.contrib.sites``
            is installed, this may be an instance of either
            ``django.contrib.sites.models.Site`` (if the sites
            application is installed) or
            ``django.contrib.sites.models.RequestSite`` (if
            not). Consult the documentation for the Django sites
            framework for details regarding these objects' interfaces.

        """
        ctx_dict = {'activation_key': self.activation_key,
                    'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
                    'site': site}
        subject = render_to_string('registration/activation_email_subject.txt',
                                   ctx_dict)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())

        message = render_to_string('registration/activation_email.txt',
                                   ctx_dict)

        self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
    def get_profile(self):
        return  self



from django.db.utils import IntegrityError


