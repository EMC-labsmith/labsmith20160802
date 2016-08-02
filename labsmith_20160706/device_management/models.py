from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    link = models.URLField(max_length=1000,blank=True,null=True)
    lock = models.BooleanField(default=False)
    owner = models.ForeignKey(User,related_name="owner_user",blank=True,null=True)
    wanted = models.ForeignKey(User,related_name="wanted_user",blank=True,null=True)
    user = models.CharField(max_length=70,blank=True,null=True)
    info = models.CharField(max_length=1000,blank=True,null=True)
    model = models.CharField(max_length=300,blank=True,null=True)
    port = models.CharField(max_length=30,blank=True,null=True)
    port_ip = models.CharField(max_length=20,blank=True,null=True)
    dvt_evt = models.CharField(max_length=30,blank=True,null=True)
    drive_1225 = models.CharField(max_length=30,blank=True,null=True)
    spa_ip = models.CharField(max_length=20,blank=True,null=True)
    spb_ip = models.CharField(max_length=20,blank=True,null=True)
    cs0_ip = models.CharField(max_length=17,blank=True,null=True)
    cs1_ip = models.CharField(max_length=17,blank=True,null=True)
    hostpc_ip = models.CharField(max_length=17,blank=True,null=True)
    server_os = models.CharField(max_length=30,blank=True,null=True)
    server_vms = models.CharField(max_length=30,blank=True,null=True)
    vendor_model_name = models.CharField(max_length=30,blank=True,null=True)
    spa_mac = models.CharField(max_length=17,blank=True,null=True)
    spb_mac = models.CharField(max_length=17,blank=True,null=True)
    mgmt_ip = models.CharField(max_length=20,blank=True,null=True)
    spa_term = models.CharField(max_length=30,blank=True,null=True)
    spb_term = models.CharField(max_length=30,blank=True,null=True)
    bmc_spa_ip =models.CharField(max_length=20,blank=True,null=True)
    bmc_spb_ip=models.CharField(max_length=20,blank=True,null=True)
    platform_type = models.CharField(max_length=30,blank=True,null=True)
    comment = models.CharField(max_length=1000,blank=True,null=True)
    status = models.CharField(max_length=300,blank=True,null=True)
    pxeFilePath = models.CharField(max_length=300,blank=True,null=True)
    holdingTime = models.CharField(max_length=300,blank=True,null=True)
    Location = (('Rack1', 'Rack1'), ('Rack2', 'Rack2'), ('Rack3', 'Rack3'), ('Rack4', 'Rack4'))
    Device_location = models.CharField(max_length=20, choices=Location, blank=True, null=True)
    def __unicode__(self):
        return self.name

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    msg = models.CharField(max_length=100)
    device = models.ForeignKey(Device)
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField()
    def __unicode__(self):
        return self.user.get_full_name() +" "+  self.msg + " " +  self.device.name + " at " + self.timestamp.strftime("%A, %d. %B %Y %I:%M%p")

class MaintainLog(models.Model):
    id = models.AutoField(primary_key=True)
    MachineName = models.CharField(max_length=30)
    user = models.CharField(max_length=20,blank=True,null=True)
    timestamp=models.DateTimeField()
    content = models.CharField(max_length=1000,blank=True,null=True)
    # countNumber = models.CharField(max_length=30,blank=True,null=True)
    def __unicode__(self):
        return self.MachineName + " " + self.user+" " + "at"+ " "+self.timestamp.strftime("%A, %d. %B %Y %I:%M%p")


class UsageLog(models.Model):
    id = models.AutoField(primary_key=True)
    machineName = models.CharField(max_length=30)
    user = models.CharField(max_length=20,blank=True,null=True)
    reserveTimestamp=models.DateTimeField()
    #holdingTime = models.DateTimeField()
    releaseTimestamp=models.DateTimeField()
    port = models.CharField(max_length=30,blank=True,null=True)
    isUse = models.CharField(max_length=1000,blank=True,null=True)
    # countNumber = models.CharField(max_length=30,blank=True,null=True)
    def __unicode__(self):
        return self.user + " used " + self.machineName + " form "+ \
               self.reserveTimestamp.strftime("%A, %d. %B %Y %I:%M%p") + " to " + \
               self.releaseTimestamp.strftime("%A, %d. %B %Y %I:%M%p")



class SlicSfp(models.Model):
    id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=30,blank=True,null=True)
    owner = models.ForeignKey(User,related_name="SlicSfp_owner_user",blank=True,null=True)
    user = models.CharField(max_length=20,blank=True,null=True)
    PN = models.CharField(max_length=300,blank=True,null=True)
    comment = models.CharField(max_length=1000,blank=True,null=True)
    # info = models.CharField(max_length=1000,blank=True,null=True)
    total_number = models.CharField(max_length=30,blank=True,null=True)
    reserved_number = models.CharField(max_length=30,blank=True,null=True)
    def __unicode__(self):
        return self.model_name

class SlicSfpInfo(models.Model):
    id = models.AutoField(primary_key=True)
    MachineName = models.CharField(max_length=30)
    user = models.CharField(max_length=20,blank=True,null=True)
    time=models.DateTimeField()
    reserve_number = models.CharField(max_length=30,blank=True,null=True)
    release_number = models.CharField(max_length=30,blank=True,null=True)
    info = models.CharField(max_length=1000,blank=True,null=True)
    # available_number = models.CharField(max_length=30,blank=True,null=True)
    def __unicode__(self):
        return self.MachineName
        # return "%s %s is reserved by %s at %s." % (self.number,self.MachineName,self.user,self.timestamp.strftime("%d. %B %Y"))     
