from django.db import models
from django.db.models import DO_NOTHING


class Account(models.Model):
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.number


class Owner(models.Model):
    accounts = models.ManyToManyField(Account, through='OwnerAccount')
    fullName = models.TextField()

    def __str__(self):
        return self.fullName


class OwnerAccount(models.Model):
    owner = models.ForeignKey(Owner, on_delete=DO_NOTHING)
    account = models.ForeignKey(Account, on_delete=DO_NOTHING)

    def __str__(self):
        return self.owner


class Transaction(models.Model):
    owner_account = models.ForeignKey(OwnerAccount, on_delete=DO_NOTHING)
    title = models.CharField('title', max_length=50)

    def __str__(self):
        return self.title
