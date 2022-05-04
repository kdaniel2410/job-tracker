from django.contrib import admin
from . import models

admin.site.register(models.Job)
admin.site.register(models.Shift)
admin.site.register(models.Reimbursement)
admin.site.register(models.Expense)
admin.site.register(models.Target)
