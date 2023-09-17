from django.db import models
from .const import GENDER_CHOICES

def upload_path(self, filename):
    try: 
        path = f"photos/{self.__class__.__name__}/{self.stu_id}.jpg"
    except Exception as e:
        print("-----------------------")
    return str(path)

class Student(models.Model):
    stu_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=100)
    mobile_no = models.BigIntegerField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
    permanent_address = models.CharField(max_length=250)
    current_address = models.CharField(max_length=250)
    country = models.IntegerField()
    state = models.IntegerField()
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)  
    photo = models.ImageField(upload_to=upload_path)