from django.db import models
import datetime

class StatusChoice(models.TextChoices):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'

class OrderStatusChoice(models.TextChoices):
    PENDING = 'Pending'
    PARTIAL = 'Partial'
    COMPLETED = 'Completed'

class PaymentTypeChoice(models.TextChoices):
    DEBIT = 'Debit'
    CREDIT = 'Credit'

class VoucherTypeChoice(models.TextChoices):
    PAYMENT = 'Payment'
    RECEIPT = 'Receipt'
    JOURNAL = 'Journal'
    CONTRA = 'Contra'

class MonthChoice(models.IntegerChoices):
    JANUARY = 1, 'January'
    FEBRUARY = 2, 'February'
    MARCH = 3, 'March'
    APRIL = 4, 'April'
    MAY = 5, 'May'
    JUNE = 6, 'June'
    JULY = 7, 'July'
    AUGUST = 8, 'August'
    SEPTEMBER = 9, 'September'
    OCTOBER = 10, 'October'
    NOVEMBER = 11, 'November'
    DECEMBER = 12, 'December'


class YearChoices(models.IntegerChoices):
    def year_choices():
        return [(r,r) for r in range(2000, datetime.date.today().year+100)] 