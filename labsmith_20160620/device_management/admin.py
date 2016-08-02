from django.contrib import admin
from .models import Device, Log, MaintainLog,SlicSfp,SlicSfpInfo



# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'port', 'lock', 'link', 'owner', 'info')
class SlicSfpInfoAdmin(admin.ModelAdmin):
    list_display = ('MachineName', 'user', 'reserve_number','release_number','info','time')
    list_filter = ('MachineName','user')
admin.site.register(Device, DeviceAdmin)
admin.site.register(Log)
admin.site.register(MaintainLog)
# admin.site.register(NPEDevice)
admin.site.register(SlicSfp)
admin.site.register(SlicSfpInfo,SlicSfpInfoAdmin)

