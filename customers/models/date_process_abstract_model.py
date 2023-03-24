from django.db import models


class DateProcessModel(models.Model):
    """
    Abstract model that add fields 'created_at' and 'updated_at'
    """
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Date of creation")
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name="Date of last update")

    class Meta:
        abstract = True
