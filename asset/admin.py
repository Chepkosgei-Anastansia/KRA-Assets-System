from django.contrib import admin

# Register your models here.
from .models import Station, Department, Section, User, Asset,Ticket, DeployedAsset, Staff


admin.site.register(Station)
admin.site.register(Department)
admin.site.register(Section)
admin.site.register(User)
admin.site.register(Asset)
admin.site.register(Ticket)
admin.site.register(DeployedAsset)
admin.site.register(Staff)
