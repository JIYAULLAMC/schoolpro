from django.db import models
from .. import consts
from django.utils.translation import gettext as _
from student import consts as st_consts
from .curiculam_models import Curiculam

def upload_path(self, filename):
    try: 
        path = f"photos/{self.__class__.__name__}/{self.inst_id}.jpg"
    except Exception as e:
        print("-----------------------")
    return str(path)

class Institute(models.Model):
    inst_id = models.CharField(_("inst_id"), unique=True, max_length=consts.MAX_INST_ID)
    inst_name = models.CharField(_("inst_name"), max_length=consts.MAX_INST_NAME )
    inst_curiculams = models.ManyToManyField(Curiculam)
    inst_email = models.EmailField(_("inst_email"), max_length=consts.MAX_INST_EMAIL, blank=True, null=True)
    contact_no = models.BigIntegerField(_("inst_contact_no"), )
    address = models.CharField(_("inst_address"), max_length=consts.MAX_INST_ADDRESS, blank=True, null=True)
    country = models.IntegerField(_("inst_country"), default="India", blank=True, null=True)
    state = models.IntegerField(_("inst_state"), choices=st_consts.INDIAN_STATES_UNION_TRS, blank=True, null=True)
    city = models.CharField(_("inst_city"), max_length=consts.MAX_INST_CITY, blank=True, null=True)
    pin_code = models.CharField(_("inst_pin_code"), max_length=consts.MAX_INST_PIN_CODE, blank=True, null=True)  
    photo = models.ImageField(_("inst_photo"), upload_to=upload_path, blank=True, null=True)

    def __str__(self):
        return f"{self.inst_id}_{self.inst_name}"