# -*- coding: cp1252 -*-
from django.contrib import admin

from modulos.perfiles.models import Perfil

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Perfil

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    #fieldsets = UserAdmin.fieldsets + (            (None, {'fields': ('some_extra_data',)}),    )







from django.contrib.auth.models import Group
admin.site.unregister(Group)
admin.site.register(Perfil, MyUserAdmin)

