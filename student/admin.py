from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ["id", "stu_id", "first_name", "last_name", "date_of_birth", "email", "mobile_no", "gender", "permanent_address", "current_address", "country", "state", "city", "pin_code", "photo",]