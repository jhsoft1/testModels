from django.db import models
from django.db.models import DO_NOTHING


class Whisky(models.Model):
    whisky = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.whisky


class User(models.Model):
    user = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.user


class DateWhisky(models.Model):
    date = models.DateField(primary_key=True)
    whisky = models.ManyToManyField('Whisky')

    def __str__(self):
        return str(self.date)


class DateUser(models.Model):
    date = models.OneToOneField('DateWhisky', on_delete=DO_NOTHING)
    user = models.ManyToManyField('User')

    def __str__(self):
        return str(self.date)


class DateUserWhisky(models.Model):
    dateuser = models.OneToOneField('DateUser', on_delete=DO_NOTHING)
    # date = models.OneToOneField('Date', on_delete=DO_NOTHING)
    # user = models.OneToOneField('User', on_delete=DO_NOTHING)
    whisky = models.ManyToManyField('Whisky')
    nose = models.IntegerField()
    taste = models.IntegerField()

    def __str__(self):
        return str(self.whisky)
