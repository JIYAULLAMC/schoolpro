from django.db import models
from . import consts
from django.utils.translation import gettext as _

def upload_path(self, filename):
    try: 
        path = f"photos/{self.__class__.__name__}/{self.stu_id}.jpg"
    except Exception as e:
        print("-----------------------")
    return str(path)

class Student(models.Model):
    stu_id = models.CharField(_("stu_id"), max_length=20, unique=True )
    first_name = models.CharField(_("stu_first_name"), max_length=consts.MAX_STU_FIRST_NAME)
    last_name = models.CharField(_("stu_last_name"), max_length=consts.MAX_STU_LAST_NAME, blank=True, null=True)
    date_of_birth = models.DateField(_("stu_date_of_birth"), blank=True, null=True)
    standard = models.IntegerField(_("stu_standard"), choices=consts.STANDARD_CHOICES)
    email = models.EmailField(_("stu_email"), max_length=consts.MAX_STU_EMAIL, blank=True, null=True)
    mobile_no = models.BigIntegerField(_("stu_mobile_no"), )
    gender = models.IntegerField(_("stu_gender"), choices=consts.GENDER_CHOICES, blank=True, null=True)
    permanent_address = models.CharField(_("stu_permanent_address"), max_length=consts.MAX_STU_PERMANENT_ADDRESS, blank=True, null=True)
    current_address = models.CharField(_("stu_current_address"), max_length=consts.MAX_STU_CURRENT_ADDRESS, blank=True, null=True)
    country = models.IntegerField(_("stu_country"), default="India", blank=True, null=True)
    state = models.IntegerField(_("stu_state"), choices=consts.INDIAN_STATES_UNION_TRS, blank=True, null=True)
    city = models.CharField(_("stu_city"), max_length=consts.MAX_STU_CITY, blank=True, null=True)
    pin_code = models.CharField(_("stu_pin_code"), max_length=consts.MAX_STU_PIN_CODE, blank=True, null=True)  
    photo = models.ImageField(_("stu_photo"), upload_to=upload_path, blank=True, null=True)