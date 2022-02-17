from django.contrib import admin

from .models import Person, Group, Membership, Test

admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Test)
