from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def transfer_funds(self, to_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            to_account.balance += amount
            self.save()
            to_account.save()
            return True
        return False