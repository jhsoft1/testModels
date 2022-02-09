from django.contrib import admin

from .models import Whisky, User, DateWhisky, DateUser, DateUserWhisky

admin.site.register(Whisky)
admin.site.register(User)
admin.site.register(DateWhisky)
admin.site.register(DateUser)
admin.site.register(DateUserWhisky)
