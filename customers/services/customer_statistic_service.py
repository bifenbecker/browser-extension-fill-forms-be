from customers.models import CustomerStatistic, CustomUser, CustomerDictSettings


class CustomerStatisticService:

    @classmethod
    def get_successfully_filled_fields_on_sites(cls, user: CustomUser) -> dict:
        """
        Return statistic: How much times extension filled which fields on which site
        Related to settings, not user
        :param user: Customer
        :type user: CustomUser
        :return: Collected data
        :rtype: dict
        """

        settings = user.settings
        statistic = settings.statistic.filter(success=True)
