from django.contrib import admin
from .models import Institute


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
	list_display = ["id", "inst_id", "inst_name", "category", "inst_email", "contact_no",  "country", "state", "city", "pin_code",  "address", "photo"]

	fieldsets = (
		('Basic Information', {
			'fields': (('inst_id', 'category'),),
		}),
		('Additional Information', {
			'fields': (('inst_name', ))
		}),
		('Additional Information', {
			'fields': (('contact_no', 'inst_email'), ('country', 'state', "city", "pin_code"),)
		}),
		('Additional Information', {
			'fields': (('address', "photo"),)
		}),
	)