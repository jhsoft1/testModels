from django.contrib.auth.models import User
from django.db import models
from django.db.models import DO_NOTHING, UniqueConstraint, CheckConstraint, Q, ForeignKey


class Whisky(models.Model):
    name = models.CharField(max_length=128, primary_key=True)

    class Meta:
        verbose_name_plural = "Whiskies"

    def __str__(self):
        return self.name


class Evening(models.Model):
    date = models.DateField(primary_key=True)
    whiskies = models.ManyToManyField(Whisky, through='EveningWhisky')

    def __str__(self):
        return str(self.date)


class EveningWhisky(models.Model):
    evening = ForeignKey(Evening, on_delete=DO_NOTHING)
    whisky = ForeignKey(Whisky, on_delete=DO_NOTHING)

    class Meta:
        verbose_name_plural = "EveningWhiskies"
        constraints = [UniqueConstraint(fields=['evening', 'whisky'], name='evening_whisky')]

    def __str__(self):
        return str(self.evening) + ' ' + str(self.whisky)


class Tasting(models.Model):
    evening_whisky = ForeignKey(EveningWhisky, on_delete=DO_NOTHING)
    nose = models.DecimalField("nose/Geruch (0-10)", max_digits=3, decimal_places=1)
    taste = models.DecimalField("taste/Geschmack (0-10)", max_digits=3, decimal_places=1)
    user = ForeignKey(User, on_delete=DO_NOTHING)

    class Meta:
        constraints = [UniqueConstraint(fields=['evening_whisky', 'user'], name='evening_whisky_user'),
                       CheckConstraint(check=Q(nose__gte=0) & Q(nose__lte=10), name='nose_between_0_10'),
                       CheckConstraint(check=Q(taste__gte=0) & Q(taste__lte=10), name='taste_between_0_10')]

    def __str__(self):
        return str(self.evening_whisky) + ' ' + str(self.user)
