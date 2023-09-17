from django.db import models
from .. import consts
from django.utils.translation import gettext as _


class Curiculam(models.Model):
    cclm_id = models.CharField(_("cclm_id"), unique=True, max_length=consts.MAX_CURICULAM_ID)
    cclm_name = models.IntegerField(_("cclm_name"), unique=True, choices=consts.CURCULAM_CATEGORY)
    cclm_duration_year = models.IntegerField(_("cclm_duration_year"), default=0)
    cclm_duration_month = models.IntegerField(_("cclm_duration_month"), default=0)                                                
    cclm_duration_day = models.IntegerField(_("cclm_duration_day"), default=0)

                                                