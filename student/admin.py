from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ["id", "stu_id", "first_name", "last_name", "date_of_birth", "standard", "email", "mobile_no", "gender", "permanent_address", "current_address", "country", "state", "city", "pin_code", "photo",]

	fieldsets = (
		('Basic Information', {
			'fields': (('stu_id', 'standard'),),
		}),
		('Additional Information', {
			'fields': (('first_name', 'last_name'), ('date_of_birth', 'gender'),)
		}),
		('Additional Information', {
			'fields': (('mobile_no', 'email'), ('country', 'state',),)
		}),
		('Additional Information', {
			'fields': (('mother_name', 'father_name'), ("parents_contact_no"),)
		}),
		('Additional Information', {
			'fields': (("photo",), ('current_address', 'permanent_address'),)
		}),
	)