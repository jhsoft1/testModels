from django.db import models
from django.db.models import DO_NOTHING
from django.contrib.auth.models import User


class Whisky(models.Model):
    whisky = models.CharField(max_length=200, primary_key=True)

    class Meta:
        verbose_name_plural = "Whiskies"

    def __str__(self):
        return self.whisky


class Evening(models.Model):
    evening = models.DateField(primary_key=True)
    whiskies = models.ManyToManyField('Whisky')

    def __str__(self):
        return str(self.evening)


class WhiskyTasting(models.Model):
    evening = models.ForeignKey('Evening', on_delete=DO_NOTHING)
    whisky = models.ForeignKey('Whisky', on_delete=DO_NOTHING)
    nose = models.IntegerField()
    taste = models.IntegerField()
    user = models.ForeignKey(User, on_delete=DO_NOTHING)

    def __str__(self):
        return str(self.whisky)  # + str(self.nose) + str(self.taste) + self.user
