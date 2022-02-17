from django.contrib import admin

from .models import Account, Owner, OwnerAccount, Transaction

admin.site.register(Account)
admin.site.register(Owner)
admin.site.register(OwnerAccount)
admin.site.register(Transaction)
