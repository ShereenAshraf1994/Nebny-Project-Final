from django.contrib import admin
from authentication.models import *
from atfaluna.models import *

class commAdmin(admin.ModelAdmin):
	list_display= ('id','name','head','get_father','get_mother','get_children','get_home')
	search_fields=('name','head')

	def get_children(self, obj):
		return "\n".join([p.name for p in obj.children.all()])
	def get_mother(self, obj):
		return "\n".join([p.name for p in obj.mother.all()])
	def get_father(self, obj):
		return "\n".join([p.name for p in obj.father.all()])
	def get_home(self, obj):
		return "\n".join([p.address for p in obj.home.all()])

	
class memberAdmin(admin.ModelAdmin):
	list_display= ('user','is_head','is_UB','faculty','is_deleted','guc_id','committie','approved','new_messages','position')
	#def get_not(self, obj):
	#	return "\n".join([p.message for p in obj.notification.all()])

class notifAdmin(admin.ModelAdmin):
	list_display= ('message','sender','reciver','is_read')

class CoreAdmin(admin.ModelAdmin):
	list_display= ('core_president','get_comm','description')

	def get_comm(self, obj):
		return "\n".join([p.name for p in obj.committies.all()])

class SuppAdmin(admin.ModelAdmin):
	list_display= ('support_president','get_comm','description')

	def get_comm(self, obj):
		return "\n".join([p.name for p in obj.committies.all()])
	
admin.site.register(Notification,notifAdmin)
admin.site.register(Committie,commAdmin)
admin.site.register(Member,memberAdmin)
admin.site.register(Core,CoreAdmin)
admin.site.register(Support,SuppAdmin)
# Register your models here.
