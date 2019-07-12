from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models

from invitations.models import Invitation


class Invitation(Invitation):
    groups = ArrayField(models.IntegerField(null=False, blank=True), null=False, default=list)
