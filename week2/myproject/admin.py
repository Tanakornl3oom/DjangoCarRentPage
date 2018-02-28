from django.contrib import admin

from myproject.models import Person,Car,Rent
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Person._meta.fields]

class RentAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Rent._meta.fields]
	list_editable = ('stop_datetime','fee')

class CarAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Car._meta.fields]

admin.site.register(Person,PersonAdmin)
admin.site.register(Rent,RentAdmin)
admin.site.register(Car,CarAdmin)
