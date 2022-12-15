from django.db import models
from customizations.choices import VoucherTypeChoice

class AccountType(models.Model):
    title = models.CharField('Type', max_length=30)

class AccountGroup(models.Model):
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE, related_name='groups', verbose_name='Account Type')
    title = models.CharField('Group', max_length=30)

class ChartOfAccount(models.Model):
    account_group = models.ForeignKey(AccountGroup, on_delete=models.CASCADE, related_name='groups', verbose_name='Account Group') 
    title = models.CharField('Type', max_length=30)

class Voucher(models.Model):
    voucher_type = models.CharField('Type', max_length=20, choices=VoucherTypeChoice.choices, default=VoucherTypeChoice.PAYMENT)
    voucher_number = models.CharField('Voucher No.', max_length=50)
    voucher_date = models.DateField('Voucher Date', auto_now_add=True)
    narration = models.CharField('Narration', max_length=150)

class GeneralLedger(models.Model):
    ledger_date = models.DateField('Ledger Date', auto_now_add=True)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE, related_name='ledgerentries', verbose_name='Voucher')
    account = models.ForeignKey(ChartOfAccount, on_delete=models.CASCADE, related_name='ledgerentries', verbose_name='Account')
    debit = models.IntegerField('Debit', default=0)
    credit = models.IntegerField('Credit', default=0)
    narration = models.CharField('Narration', max_length=150)

