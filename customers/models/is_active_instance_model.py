from django.db import models


class IsActiveModel(models.Model):
    """
    Abstract model that add field 'is_active'
    """
    is_active = models.BooleanField(verbose_name="Is active object from list of Customer's settings", default=False)

    class Meta:
        abstract = True
