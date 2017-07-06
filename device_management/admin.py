from django.contrib import admin
from .models import Device, Log, MaintainLog,SlicSfp,SlicSfpInfo
from django.contrib.admin.models import LogEntry
from django.contrib.admin.options import ModelAdmin
import datetime


def my_construct_change_message (self, request, form, formsets):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        change_message = ['User from %s. Changed at %s.' % (ip, str(datetime.datetime.now())[:-7])]
        if form.changed_data:
            for data in form.changed_data:
                try:
                    toData = form.data[data]
                except:
                    toData = 'off'
                fromData = form.initial[data]
                if not fromData:
                    fromData = 'empty'
                if not toData:
                    toData = 'empty'
                change_message.append('Changed %s from %s to %s. ' % (data, fromData, toData))

        if formsets:
            for formset in formsets:
                for added_object in formset.new_objects:
                    change_message.append('Added %(name)s "%(object)s".' % {'name': added_object._meta.verbose_name, 'object': added_object})
                for changed_object, changed_fields in formset.changed_objects:
                    change_message.append('Changed %(list)s for %(name)s "%(object)s".'
                                          % {'list': changed_fields,
                                             'name': changed_object._meta.verbose_name,
                                             'object': changed_object})
                for deleted_object in formset.deleted_objects:
                    change_message.append('Deleted %(name)s "%(object)s".'
                                          % {'name': deleted_object._meta.verbose_name,
                                             'object': deleted_object})
        change_message = ' '.join(change_message)
        return change_message or 'No fields changed.'

ModelAdmin.construct_change_message = my_construct_change_message

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
admin.site.register(LogEntry)
