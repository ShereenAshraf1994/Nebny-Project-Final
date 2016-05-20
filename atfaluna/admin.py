from django.contrib import admin
from atfaluna.models import *



class ChildrenAdmin(admin.ModelAdmin):
	list_display= ('id','name','birthdate','education_level','school_name','doros_number','doros_type','doros_expenses','doros_needed','is_graduate',
		'gradutae_degree','is_worker','salary','per','is_sick','disease','medecine','health_care_expenses','health_care_paid_by','want_kashf',
		'is_atraf_sena3eya','is_3aseel_kalawy','is_surgery_needed','is_special_needs','health_care_needed','education_needed','economic_development_needed',
		'relif_needed')

	

class ParentAdmin(admin.ModelAdmin):
	list_display= ('id','name','birthdate','age','education_level','is_3a2el','job','job_status','marital_status','national_id','mobile','work_status','salary','is_sick',
	'disease','medecine','health_care_expenses','health_care_paid_by','want_kashf','is_atraf_sena3eya','is_3aseel_kalawy','is_surgery_needed','is_special_needs',
	'want_project','project_idea','project_cost','project_profit','project_notes','health_care_needed','education_needed','economic_development_needed')
	

class HomeAdmin(admin.ModelAdmin):
	list_display= ('id','building_status','wall_status','roof_status','floor_status','kitchen','toilet','sarf_sehy','water_shabaka','electrical_equipments_needed',
		'electrical_equipments_radee2a','furniture_needed','furniture_radee2','living_rooms_no','address','relif_needed')

class FamilyAdmin(admin.ModelAdmin):
	list_display= ('id','home','father','mother','get_children','poverty_level','family_members','other_members','other_notes','is_member_ommi','ommi','ommi_free_time','is_ma3ashat_sho2on_egtma3eya',
	'is_ma3ashat_ta2meneya','masdar_da5l','get_installment','food_expenses','transportation_expenses','education_expenses','total_health_care_expenses',
	'electricity_expenses','water_expenses','mobile_expenses','rent_expenses','gas_expenses','smoking_expenses','is_tamweneya_card','no_people_in_tamweneya_card'
	,'member')

	def get_children(self, obj):
		return "\n".join([p.name for p in obj.children.all()])

	def get_installment(self, obj):
		return "\n".join([p.name for p in obj.installment.all()])

class InstallmentAdmin(admin.ModelAdmin):
	list_display= ('id','name','no_installments_left','installment_value')


admin.site.register(Children,ChildrenAdmin)
admin.site.register(Parent,ParentAdmin)
admin.site.register(Home,HomeAdmin)
admin.site.register(Family,FamilyAdmin)
admin.site.register(Installment,InstallmentAdmin)