from django.contrib import admin

from .models import Whisky, Evening, EveningWhisky, Tasting

admin.site.register(Whisky)
admin.site.register(Evening)
admin.site.register(EveningWhisky)
admin.site.register(Tasting)
