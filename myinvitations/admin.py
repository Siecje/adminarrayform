from django.contrib import admin

from invitations.admin import InvitationAdmin

from myinvitations.models import MyInvitation


class MyInvitationAdmin(InvitationAdmin):
    list_display = ['email', 'inviter', 'accepted', 'key_expired']
    fields = ["email", "inviter", "groups", "accepted",  "key", "sent"]
    readonly_fields = ("key_expired", "key",)

    def key_expired(self, obj):
        return obj.key_expired()

admin.site.unregister(MyInvitation)
admin.site.register(MyInvitation, MyInvitationAdmin)
