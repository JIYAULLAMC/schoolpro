from django.contrib import admin
from ..models import Curiculam


@admin.register(Curiculam)
class CuriculamAdmin(admin.ModelAdmin):
	list_display = ["id", "cclm_id", "cclm_name", "cclm_duration_year", "cclm_duration_month", "cclm_duration_day" ]

	fieldsets = (
		('Basic Information', {
			'fields': (('cclm_id', 'cclm_name'),),
		}),
		('Additional Information', {
			'fields': (('cclm_duration_year', 'cclm_duration_month'),("cclm_duration_day"))
		}),
	)