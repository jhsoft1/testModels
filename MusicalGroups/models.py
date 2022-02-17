from django.contrib.auth.models import User
from django.db import models
from django.db.models import DO_NOTHING


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return str(self.group) + ' ' + str(self.person)


class Test(models.Model):
    test = models.ForeignKey(Membership, on_delete=DO_NOTHING)
    comment = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=DO_NOTHING)

    def __str__(self):
        return str(self.test) + ' ' + str(self.comment) + ' ' + str(self.user)
