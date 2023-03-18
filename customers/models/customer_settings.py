from django.db import models
from .custom_user import CustomUser
from .date_process_abstract_model import DateProcessModel


class CustomerDictSettings(DateProcessModel):
    """
    General settings of customer extension
    """
    customer = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="settings",
                                    verbose_name="Customer's settings")
    email_address = models.EmailField(null=False, blank=False,
                                      verbose_name="Customer's email address")
    first_name = models.CharField(null=False, blank=False, max_length=20, verbose_name="Customer's name")
    last_name = models.CharField(null=False, blank=False, max_length=30, verbose_name="Customer's last name")

    mobile_number = models.CharField(null=False, blank=False, max_length=30, verbose_name="Customer's mobile number")
    isAgreeSendMessagesOnEmail = models.BooleanField(default=False, verbose_name="Does customer agree on mailing list")

    def __str__(self):
        return self.email_address

    def get_full_name_customer(self) -> str:
        """
        Build string of first name and last name customer
        :return: first name and last name
        :rtype: string
        """
        return f"{self.first_name} {self.last_name}"


class CustomerAddress(DateProcessModel):
    """
    Model describe customer's address
    """
    customer_settings = models.ForeignKey(CustomerDictSettings, on_delete=models.CASCADE, related_name="addresses",
                                          verbose_name="Customer's addresses")
    country = models.CharField(null=False, blank=False, max_length=30, verbose_name="Country where customer lives")
    city = models.CharField(null=False, blank=False, max_length=20, verbose_name="City where customer lives")
    street = models.CharField(null=False, blank=False, max_length=20, verbose_name="Street where customer lives")
    house_number = models.CharField(null=False, blank=False, max_length=10,
                                    verbose_name="House number customer's address")
    flat_number = models.PositiveIntegerField(null=True, blank=True, default=None,
                                              verbose_name="Flat number customer's address")
    postal_code = models.CharField(null=False, blank=False, max_length=20, verbose_name="Customer's postal code")


class CustomerPaymentMethod(DateProcessModel):
    """
    Model describe customer's payment method credit card
    """
    customer_settings = models.ForeignKey(CustomerDictSettings, on_delete=models.CASCADE, related_name="payment_cards",
                                          verbose_name="Customer's payment cards")
    card_number = models.CharField(null=False, blank=False, max_length=16,
                                   verbose_name="Customer's payment method card number")
    expire_date = models.DateField(null=False, blank=False)
