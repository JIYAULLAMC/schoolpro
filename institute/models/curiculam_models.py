from django.db import models
from .. import consts
from django.utils.translation import gettext as _


class Curiculam(models.Model):
    cclm_id = models.IntegerField(_("cclm_id"), unique=True)
    cclm_name = models.CharField(_("cclm_name"),max_length=consts.MAX_CURICULAM_NAME, unique=True, choices=consts.CURCULAM_CATEGORY)
    cclm_duration_year = models.IntegerField(_("cclm_duration_year"), default=0)
    cclm_duration_month = models.IntegerField(_("cclm_duration_month"), default=0)                                                
    cclm_duration_day = models.IntegerField(_("cclm_duration_day"), default=0)

    def __str__(self):
        return f"{self.cclm_id}_{self.cclm_name}"
                                                