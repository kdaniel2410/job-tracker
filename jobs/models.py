from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    hourly_rate = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Shift(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    start = models.DateTimeField()
    length = models.FloatField(default=0)

    def __str__(self):
        return f"{self.length} hours on {self.start}"

    class Meta:
        ordering = ['start']


class Reimbursement(models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.amount


class Expense(models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.amount


class Target(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE)
    amount = models.FloatField(default=1000)
    shifts_per_week = models.IntegerField(default=4)

    def __str__(self):
        return self.amount
