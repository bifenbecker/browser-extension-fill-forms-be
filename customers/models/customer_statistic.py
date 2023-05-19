from django.db import models
from .date_process_abstract_model import DateProcessModel
from .customer_settings import CustomerDictSettings


class CustomerStatistic(DateProcessModel):
    settings = models.ForeignKey(CustomerDictSettings, on_delete=models.CASCADE, related_name="statistic",
                                 verbose_name="Customer's statistic")
    success = models.BooleanField(default=False, verbose_name="Did extension fill successfully")
    price = models.DecimalField(null=True, default=None, max_digits=6, decimal_places=2, verbose_name="Order's price")
    site = models.CharField(null=True, default=None, max_length=64, verbose_name="Site")


class FillField(models.Model):
    name = models.CharField(max_length=32, verbose_name="Field's name")
    is_filled = models.BooleanField(default=False, verbose_name="Was field filled")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Date of creation")
    statistic = models.ForeignKey(CustomerStatistic, on_delete=models.CASCADE, related_name="fields",
                                  verbose_name="Filled fields")
