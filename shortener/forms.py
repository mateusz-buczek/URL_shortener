from django import forms

from .models import Addresses


class AddressesForm(forms.ModelForm):
    class Meta:
        model = Addresses
        fields = ('original', 'shortened')
        # help_texts = {
        #     'original': _('Paste URL here'),
        #     'shortened': _('custom short name(optional)'),
        # }
        # error_messages = {
        #     'shortened': {
        #         'max_length': _('Too long(30 chars limit)'),
        #     }
        # }
# TODO forms with validations, hook it up to html