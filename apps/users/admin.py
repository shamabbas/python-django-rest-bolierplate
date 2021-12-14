from django.contrib import admin
from django.contrib.auth.models import Group

from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
