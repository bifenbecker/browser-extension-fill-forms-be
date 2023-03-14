from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class LengthPasswordForUserValidator:
    LENGHT = 4

    def validate(self, password, user=None):
        if len(password) < self.LENGHT:
            raise ValidationError(
                _(f"This password must contain at least {self.LENGHT} characters."),
                code='password_too_short',
                params={'min_length': self.LENGHT},
            )

    def get_help_text(self):
        return _(
            f"Your password must contain at least {self.LENGHT} characters."
        )
