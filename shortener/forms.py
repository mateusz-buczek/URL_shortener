from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('original', 'shortened')
        # help_texts = {
        #     'original': _('Paste URL here'),
        #     'shortened': _('custom short name(optional)'),
        # }
        # error_messages = {
        #     'shortened': {
        #         'max_length': _('Too long(30 chars limit)'),  # TODO proper error message if name taken
        #     }
        # }


# TODO forms with validations, hook it up to html?