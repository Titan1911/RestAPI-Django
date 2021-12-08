from django.db import models

# Create your models here.
class Account(models.Model):
    # index=models.IntegerField(null=False)
    account_no=models.IntegerField(null=False)
    isActive=models.BooleanField(default=True)
    balance=models.TextField(default=0)

    def __str__(self):
        return self.account_no