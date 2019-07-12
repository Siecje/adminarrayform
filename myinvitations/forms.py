from django import forms
from invitations.forms import CleanEmailMixin
from django.utils.translation import ugettext_lazy as _

from myinvitations.models import MyInvitation

class CustomInvitationAdminAddForm(forms.ModelForm, CleanEmailMixin):
    email = forms.EmailField(
        label=_("E-mail"),
        required=True,
        widget=forms.TextInput(attrs={"type": "email", "size": "30"}))

    class Meta:
        model = MyInvitation
        fields = ("email", "inviter")

    def save(self, *args, **kwargs):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        groups = cleaned_data.get("groups")
        params = {
            'email': email,
            'groups': groups,
        }
        if cleaned_data.get("inviter"):
            params['inviter'] = cleaned_data.get("inviter")
        instance = MyInvitation.create(**params)
        instance.send_invitation(self.request)
        super().save(*args, **kwargs)
        return instance
