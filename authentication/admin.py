from django.contrib import admin
from .models import Committie

class commAdmin(admin.ModelAdmin):
	list_display= ('name','head','get_mem')
	search_fields=('name','head')

	def get_mem(self, obj):
		return "\n".join([p.first_name for p in obj.member.all()])

admin.site.register(Committie,commAdmin)
# Register your models here.
