from django.utils import timezone
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,BaseUserManager,AnonymousUser
from .models import Device,Log, MaintainLog,UsageLog,SlicSfp,SlicSfpInfo

from post_office import mail
from django.core.mail import send_mail,EmailMessage
from django.core.urlresolvers import reverse
import os
import re
import subprocess
import time
# Create your views here

def debug_call(*args, **kwargs):
    print args, kwargs
subprocess.call = debug_call

# @login_required(login_url="/login/")
def hello(req):
    currentuser = req.user
    if(req.GET.has_key('tab')):
        tabOption = req.GET['tab']
    else:
        tabOption = 'Oberon'
    print "tabOption: " + tabOption
    msg=""

    if 'id' in req.GET and 'action' in req.GET and req.GET['id']:
        transfer_name = re.compile(r'[a-zA-Z]')
        transfer_name = transfer_name.match(req.GET['action'])
        if req.GET['action']=='0':
            msg = reserve_dev(int(req.GET['id']), currentuser)
        elif req.GET['action']=='1':
            msg = want_dev(int(req.GET['id']), currentuser)
        elif req.GET['action']=='2':
            msg = release_dev(int(req.GET['id']), currentuser)
        elif req.GET['action']==transfer_name:
            transfer_name=req.POST['transfer_owner']
            msg = release_dev(int(req.GET['id']), currentuser)
            msg = reserve_dev(int(req.GET['id']), transfer_name)
        else:
            msg = "error"
    users = []
    users1 = User.objects.order_by("first_name")
    for user in users1:
        if currentuser.username != '' and user.get_full_name() and user.get_full_name() != currentuser.get_full_name():#admin has no full name
            users.append(user.get_full_name())

    devices1 = Device.objects.filter(name__startswith="OB-S").order_by("name")
    devices2 = Device.objects.filter(name__startswith="BC").order_by("name")
    devices5 = Device.objects.filter(name__startswith="PDU").order_by("name")
    devices4 = Device.objects.filter(name__startswith="JF").order_by("name")|Device.objects.filter(name__startswith="MT").order_by("name")|Device.objects.filter(name__startswith="VX").order_by("name")
    devices3 = Device.objects.filter(name__startswith="BR").order_by("name")
    devices6 = SlicSfp.objects.filter(PN__startswith="303").order_by("model_name")|SlicSfp.objects.filter(PN__startswith="019").order_by("model_name")
    devices7 = Device.objects.filter(name__startswith="H-0")
    devices8 = Device.objects.filter(name__startswith="SW")
    devices9 = Device.objects.filter(name__startswith="OB DAE").order_by("name")
    devices10 = Device.objects.filter(name__startswith="KVM").order_by("name")|Device.objects.filter(name__startswith="IO-IP").order_by("name")
    devices = [devices1,devices2,devices3,devices4,devices9,devices10]
    for i in range(-1, 6):
        for device in devices[i]:
            if device.owner:
                print device.owner
                usagelog = UsageLog.objects.get(machineName=device.name, port=device.port,
                                                user=device.owner.get_full_name(), isUse='f')
                if usagelog:
                    device.holdingTime = (timezone.now() - usagelog.reserveTimestamp).days + 1
                    device.save()
            else:
                device.holdingTime = ''
                device.save()
    #deviceusers = User.objects.order_by("first_name")
    context = {'devices1': devices1,
               'devices2': devices2,
               'devices3': devices3,
               'devices4': devices4,
               'devices5': devices5,
               'devices6': devices6,
               'devices7': devices7,
               'devices8': devices8,
               'devices9': devices9,
               'devices10': devices10,
               'users': users,
               'currentuser' : currentuser,
               'tab' : tabOption,
               'msg': msg,
               # 'deviceusers':deviceusers,
    }
    #return render_to_response('hello.html',{'devices':devices})


    return render(req, 'hello.html', context)


@login_required(login_url="/login/")
def result(req):
    if(req.GET.has_key('tab')):
        tabOption = req.GET['tab']
    else:
        tabOption = 'Oberon'
    currentuser = req.user
    if 'id' in req.GET and 'action' in req.GET and req.GET['id']:
        transfer_name = re.compile(r'[a-zA-Z]')
        if req.GET['action']=='0':
            msg = reserve_dev(int(req.GET['id']), currentuser)
        elif req.GET['action']=='1':
            msg = want_dev(int(req.GET['id']), currentuser)
        elif req.GET['action']=='2':
            msg = release_dev(int(req.GET['id']), currentuser)
        elif transfer_name.match(req.GET['action'])!=None:
            msg = release_dev(int(req.GET['id']), currentuser)
            transfer_owner = req.GET['action']
            users1 = User.objects.order_by("username")
            for user in users1:
                users = []
                users.append(user.get_full_name())
                if transfer_owner in users:
                    msg = reserve_dev(int(req.GET['id']), user)
                    break
        else:
            msg = "error"
        #msg="The button is %s and action is %s " % (req.GET['id'],req.GET['action'])

        context={"msg":msg, "tabFrom": tabOption}
        return render(req, "result.html", context)


@login_required(login_url="/login/")
def edit(req,id):
    currentuser = req.user
    device = Device.objects.get(id=id)
    print id
    if req.method == 'POST':
        device.info = req.POST['info']
        device.save()

        msg = 'change info to "%s" for' % device.info
        log=Log(device=device,user=currentuser,timestamp=timezone.now(),msg=msg)
        log.save()
        print id
        #return HttpResponseRedirect('/labsmith/?tab=Oberon')
        return redirect('/labsmith/?tab=Oberon')

        #return HttpResponseRedirect('/labsmith/')
    # context = {'device':device,}
    # return render(req,'edit.html',context)

def editBeachcomber(req,id):
    currentuser = req.user
    device = Device.objects.get(id=id)
    print id

    if req.method == 'POST':
        device.info = req.POST['info']
        device.save()

        msg = 'change info to "%s" for' % device.info
        log=Log(device=device,user=currentuser,timestamp=timezone.now(),msg=msg)
        log.save()
        print id
        print device.id
        return redirect('/labsmith/?tab=Beachcomber')

def editPDU(req,id):
    currentuser = req.user
    device = Device.objects.get(id=id)
    print id

    if req.method == 'POST':
        device.info = req.POST['info']
        device.save()

        msg = 'change info to "%s" for' % device.info
        log=Log(device=device,user=currentuser,timestamp=timezone.now(),msg=msg)
        log.save()
        print id
        print device.id
        return redirect('/labsmith/?tab=PDU|SWITCH')

def editRockies(req,id):
    currentuser = req.user
    device = Device.objects.get(id=id)
    print id

    if req.method == 'POST':
        device.info = req.POST['info']
        device.save()

        msg = 'change info to "%s" for' % device.info
        log=Log(device=device,user=currentuser,timestamp=timezone.now(),msg=msg)
        log.save()
        print id
        print device.id
        return redirect('/labsmith/?tab=Rockies')

def editBearcat(req,id):
    currentuser = req.user
    device = Device.objects.get(id=id)
    print id

    if req.method == 'POST':
        device.info = req.POST['info']
        device.save()

        msg = 'change info to "%s" for' % device.info
        log=Log(device=device,user=currentuser,timestamp=timezone.now(),msg=msg)
        log.save()
        print id
        print device.id
        return redirect('/labsmith/?tab=Bearcat')


@login_required(login_url="/login/")
def changeuser(req,id):
    currentuser = req.user

    device = Device.objects.get(id=id)
    if req.method == 'POST':
        if currentuser == device.owner:
            device.user = req.POST['user']
            device.save()

            msg = 'change user to "%s" for' % device.info
            log=Log(device=device,user=currentuser,timestamp=timezone.now(),msg=msg)
            log.save()

            return HttpResponseRedirect('/labsmith/')

    # context = {'device':device,}
    # return render(req,'edit.html',context)


@login_required(login_url="/login/")
def pxe(req,id):
    currentuser = req.user
    device = Device.objects.get(id=id)
    imageFileList = GetFileList('/images',['OS'])
   
    errors=[]
    if req.method == 'POST':

        device.pxeFilePath = req.POST['file_path']
        device.save()

        msg = "PXE is done!"
        return redirect(reverse('pxeResult',args= (id,)))

    context = {'device':device,
                   'errors':errors,
                   'imageFileList':imageFileList}
    return render(req, "pxe.html", context)

def pxeResult(req,id):
    context = {'id':id}
    return render(req, "pxeResult.html",context)

def pxeResultFile(req,id):

    device = Device.objects.get(id=id)
    # msg = " %s Done!" % device.name

    cmdstr = "/root/PXE/pxetool_web1 %s %s %s %s %s %s %s %s %s"  % (device.name, device.spa_ip, device.spb_ip, device.spa_mac, device.spb_mac, device.platform_type,device.pxeFilePath, device.bmc_spa_ip,device.bmc_spb_ip)

    f = os.popen(cmdstr)
    res = f.read()
    #print res

    # res = "OK! sdffffffffffff sdfffffffffffffffffegggggggggg sefffffffffffffffffgegggeg  gegg"

    result = res.split('!')

    context = {'result': result}
    return render(req, "pxeResultFile.html",context)

def GetFileList(FindPath,FlagStr=[]):
    FileList = []
    FileNames = os.listdir(FindPath)
    if (len(FileNames) > 0):
        for fn in FileNames :
            if(len(FlagStr) > 0):
                if(IsSubString(FlagStr,fn)):
                    fullfilename=os.path.join(FindPath,fn)
                    FileList.append(fullfilename)
            else:
                fullfilename = os.path.join(FindPath,fn)
                FileList.append(fullfilename)
            
    if(len(FileList) > 0):
        FileList.sort()

    return FileList

def IsSubString(SubStrList,Str):
    flag = True
    for substr in SubStrList:
        if not(substr in Str):
            flag=False

    return flag



def want_dev(id, currentuser):
    device = Device.objects.get(id=id)
    # subject = "[Labsmith]%s want %s" % (currentuser.get_full_name(), device.name)
    # html_msg = r'%s want your %s<br>Please kindly release it if you are no longer using it and let him/her know!<br><br><a href="http://10.62.34.99:8010/labsmith/">http://10.62.34.99:8010/labsmith/</a>' % (currentuser.get_full_name(), device.name)
    mailto = device.owner.email
    # mail.send(
        # [mailto],
        # 'alarm@labsmith.com',
        # subject=subject,
        # html_message= html_msg,
        # # priority='now',
    # )
    # from_email = 'alarm@labsmith.com'
    # msg = EmailMessage(subject,html_msg,from_email,[mailto])
    # msg.content_subtype = "html"
    # msg.send(fail_silently=False)
    # send_mail(subject, 'Here is the message.', 'alarm@labsmith.com',['Kun.Guo@emc.com'], fail_silently=False)
    curUser = currentuser.get_full_name()
    machine = device.name
    #if machine == 'PDU':
    if device.port:
        port = device.port
        subprocess.call(["/home/joe/labsmith_backup/wantmail.sh",curUser,machine, port,mailto])
    else:
        subprocess.call(["/home/joe/labsmith_backup/wantwithoutportmail.sh",curUser,machine,mailto])
    if device.wanted == None:
        msg = "An e-mail has been sent to %s for %s." % (device.owner.get_full_name(), device.name)
        device.wanted = currentuser
    else:
        msg = "The device is already wanted by %s." % (device.wanted.get_full_name())
    device.save()
    log=Log(device=device,user=currentuser,timestamp=timezone.now(),msg="want")
    log.save()
    return msg

def reserve_dev(id, currentuser):
    device = Device.objects.get(id=id)
    if device.owner:
        msg = "This device is already reserved by others, please refresh the labsmith!"
    else:    
        device.owner = currentuser
        device.save()
    # if req.method== "POST":
    #     slicsfpnum = req.POST['slicsfpNum']
    #     device.reserved_number = slicsfpnum
    #     device.save()
    #     print slicsfpnum
    #     msg = "%s is reversed by %s with %s numbers." % (device.name,currentuser.get_full_name(),device.reserved_number)
    #     return msg
    # else:
        mailto = device.owner.email
        curUser = currentuser.get_full_name()
        machine = device.name
        port = device.port
        uselog = UsageLog.objects.filter(machineName=machine)&UsageLog.objects.filter(user=curUser)&UsageLog.objects.filter(port=port)
        for log in uselog:
            if log.isUse == 'f':
                log.isUse = 't'
                log.save()
        usagelog = UsageLog()
        usagelog.machineName = machine
        usagelog.port = port
        usagelog.user = curUser
        usagelog.reserveTimestamp = timezone.now()
        usagelog.isUse = 'f'
        usagelog.releaseTimestamp = usagelog.reserveTimestamp
        usagelog.save()
        #or 'JF' in re.findall(r'JF', device.name) or 'BR' in re.findall(r'BR', device.name)
        if 'OB-S' in re.findall(r'OB-S', device.name) or 'BC' in re.findall(r'BC', device.name)or 'JF' in re.findall(r'JF', device.name)or 'BR' in re.findall(r'BR', device.name):
            subprocess.call(["/home/joe/labsmith_backup/reservemail.sh", machine, mailto])

        if port:
            msg = "%s %s is owned by %s now." % (machine, port, curUser)
        else:
            msg = "%s is owned by %s now." % (machine, curUser)
        log=Log(device=device,user=currentuser,timestamp=timezone.now(),msg="reserve")
        log.save()
    return msg

def release_dev(id, currentuser):
    device = Device.objects.get(id=id)
    mailtoowner = device.owner.email
    machine = device.name
    port = device.port
    if device.owner != currentuser and currentuser.id != 1:
        return "Your are not the owner of this device."
    else:
        device.owner = None
        device.save()
        usagelog = UsageLog.objects.get(machineName=device.name, port=device.port, isUse='f')
        usagelog.releaseTimestamp = timezone.now()
        usagelog.isUse = 't'
        usagelog.save()

        Status_spa = ''
        Status_spb = ''
        status = ''
        if 'OB-S' in re.findall(r'OB-S',device.name) or 'BC' in re.findall(r'BC',device.name):
            if 'OB-S' in re.findall(r'OB-S', device.name):
                cmdstr1 = '/root/work_pxe_test/read_oberon_mode.sh'
            else:
                cmdstr1 = '/root/work_pxe_test/read_beachcomber_mode.sh'
            f_sp = os.popen(cmdstr1)
            res_sp = f_sp.readlines()
            # print res_sp
            len_sp = len(res_sp)
            content = res_sp[4:len_sp - 1]
            length = len(content)
            # cnt = range(length)
            # print cnt
            # print length
            for i in range(length):
                text = content[i]
                item = text.split()
                if device.spa_ip == item[1] or device.spb_ip == item[1]:
                    if device.spa_ip == item[1]:
                        Status_spa = item[0] + ': ' + item[2] + ' ' + item[3]
                    else:
                        Status_spb = item[0] + ': ' + item[2] + ' ' + item[3]
                if Status_spa != '' and Status_spb != '':
                    status = Status_spa + '\n' + ' ' + Status_spb
            subprocess.call(["/home/joe/labsmith_backup/releasemailtoowner.sh", machine, mailtoowner, status])

        # subject = "[Labsmith]%s is released." % ( device.name)
        # html_msg = r'You can reserve it now.<br><br><a href="http://10.62.34.99:8010/labsmith/">http://10.62.34.99:8010/labsmith/</a>'

        if device.wanted != None:
            mailto = device.wanted.email
            device.wanted = None
            if device.port:
                subprocess.call(["/home/joe/labsmith_backup/releasemail.sh", machine, port, mailto])
            else:
                subprocess.call(["/home/joe/labsmith_backup/releasewithoutportmail.sh", machine, mailto])

        device.user = ""
        device.lock = False
        device.save();
        if device.port:
            msg = "%s %s is free now." % (device.name, device.port)
        else:
            msg = "%s is free now." % (device.name)
        log=Log(device=device,user=currentuser,timestamp=timezone.now(),msg="release")
        log.save()
        return msg



@login_required(login_url="/login/")       
def mychangePWD(req):
    error = None
    currentuser = req.user
    if req.method== "POST":
       #oldpassword = req.POST['inputOldPassword']
        newpassword = req.POST['inputNewPassword']
        newpassword2 = req.POST['inputNewPassword2']

        if newpassword != newpassword2 :
            error = "New password do not match, input again."
        else:
            user=User.objects.get(username= currentuser.username )
            user.set_password(newpassword)
            user.save()
            return HttpResponseRedirect('/labsmith/')


    context={'error':error}
    return render(req,"changePWD.html",context)

#Show the info in different pages.
@login_required(login_url="/login/")
def myOberon(req):

    currentuser = req.user
    msg=""
    if 'id' in req.GET and 'action' in req.GET and req.GET['id']:
        if req.GET['action']=='0':
            msg = reserve_dev(int(req.GET['id']), currentuser)
        elif req.GET['action']=='1':
            msg = want_dev(int(req.GET['id']), currentuser)
        elif req.GET['action']=='2':
            msg = release_dev(int(req.GET['id']), currentuser)
        else:
            msg = "error"
    devices1 = Device.objects.filter(name__startswith="OB").order_by("name")
    devices2 = Device.objects.filter(name__startswith="BC").order_by("name") 
    devices3 = Device.objects.filter(name__startswith="PDU").order_by("name")
    devices4 = Device.objects.filter(name__startswith="IO").order_by("name")
    devices5 = Device.objects.filter(name__startswith="BEARCAT").order_by("name")
    
    # deviceusers = User.objects.order_by("first_name")
    context = {'devices1': devices1,
               'devices2': devices2,
               'devices3': devices3,
               'devices4': devices4,
               'devices5': devices5,
               'currentuser' : currentuser,
               'msg': msg,
               # 'deviceusers':deviceusers,
    }



    return render(req, "Oberon.html", context)


def statusResult(req):

    currentuser = req.user
    service_mode = "Service mode"
    if(req.GET.has_key('tab')):
        tabOption = req.GET['tab']
    else:
        tabOption = 'Oberon'
	allwords=[]
    cmdstr1 = '/root/work_pxe_test/read_oberon_mode.sh'
    f_sp = os.popen(cmdstr1)  
    res_sp = f_sp.readlines()
    # print res_sp
    len_sp = len(res_sp)
    content = res_sp[4:len_sp-1]
    length = len(content)
    # cnt = range(length)
    # print cnt
    name_OB=[]
    Ip_OB = []
    Status_OB = []
    # print length
    for i in range(length):
        text=content[i]
        item=text.split()
        # print item
        name_OB.append(item[0])
        Ip_OB.append(item[1])
        Status_OB.append(item[2]+' '+item[3])
    # print name
    # print Ip
    # print Status
    # print i
    
  
    # cmdstr2 = '/root/work_pxe_test/read_bearcat_mode.sh'
    # f_sp2 = os.popen(cmdstr2)  
    # res_sp2 = f_sp2.readlines()
    # # print res_sp2
    # len_sp2 = len(res_sp2)
    # content2 = res_sp2[4:len_sp2-1]
    # length2 = len(content2)
    # # cnt = range(length)
    # # print cnt
    # name_Be=[]
    # Ip_Be = []
    # Status_Be = []
    # # print length
    # for j in range(length2):
        # text2=content2[j]
        # item2=text2.split()
        # # print item2
        # name_Be.append(item2[0])
        # # print name_Be
        # Ip_Be.append(item2[1])
        # # print Ip_Be
        # Status_Be.append(item2[2]+' '+item2[3]) 
        # # print Status_Be




    cmdstr3 = '/root/work_pxe_test/read_beachcomber_mode.sh'
    f_sp3 = os.popen(cmdstr3)  
    res_sp3 = f_sp3.readlines()
    # print res_sp3
    len_sp3 = len(res_sp3)
    content3 = res_sp3[4:len_sp3-1]
    length3 = len(content3)
    # cnt = range(length)
    # print cnt
    name_BC=[]
    Ip_BC = []
    Status_BC = []
    # print length
    for k in range(length3):
        text3=content3[k]
        item3=text3.split()
        # print item3
        name_BC.append(item3[0])
        Ip_BC.append(item3[1])
        Status_BC.append(item3[2]+' '+item3[3]) 
    
    context={
            'name_OB':name_OB,
            'Ip_OB':Ip_OB,
            'Status_OB':Status_OB,
            # 'name_Be':name_Be,
            # 'Ip_Be':Ip_Be,
            # 'Status_Be':Status_Be,
            'name_BC':name_BC,
            'Ip_BC':Ip_BC,
            'Status_BC':Status_BC,
            'tab':tabOption}
   
    return render(req,"statusResult.html",context)


def IPResult(req):

    currentuser = req.user
    service_mode = "Service mode"
    if(req.GET.has_key('tab')):
        tabOption = req.GET['tab']
    else:
        tabOption = 'Oberon'
       
    ip1 = Device.objects.filter(name__startswith="OB-S").order_by("name")
    ip6 = Device.objects.filter(name__startswith="OB DAE").order_by("name")
    ip2 = Device.objects.filter(name__startswith="BC").order_by("name") 
    ip3 = Device.objects.filter(name__startswith="JF").order_by("name")|Device.objects.filter(name__startswith="MT").order_by("name")|Device.objects.filter(name__startswith="VX").order_by("name")
    ip4 = Device.objects.filter(name__startswith="BR").order_by("name")
    ip5 = Device.objects.filter(name__startswith="H-")
    context = {'ip1': ip1,
               'ip2': ip2,
               'ip3': ip3,
               'ip4': ip4,
               'ip5': ip5,
               'ip6': ip6,
               'tab' : tabOption,
    }
   
    return render(req,"IPResult.html",context)


def mainLog(req,id):

    errors = []
    currentuser = req.user
    print currentuser

    if(req.GET.has_key('tab')):
        tabOption = req.GET['tab']
    else:
        tabOption = 'Log'
    print "tabOption: " + tabOption
    device = Device.objects.get(id=id)
   
    # maintainLogOB = MaintainLog.objects.filter(name__startswith="OB").order_by("timestamp")
    # maintainLogBC = MaintainLog.objects.filter(name__startswith="BC").order_by("timestamp")
    # maintainLogPDU = MaintainLog.objects.filter(name__startswith="PDU").order_by("timestamp")
    # maintainLogIO = MaintainLog.objects.filter(name__startswith="IOHOST").order_by("timestamp")
    # maintainLogBE = MaintainLog.objects.filter(name__startswith="BEARCAT").order_by("timestamp")
    usagelog = UsageLog.objects.filter(machineName=device.name,port=device.port).order_by("-releaseTimestamp")

    if req.method == "POST":
        if currentuser.username == '':
            return HttpResponseRedirect("/login/")
        if not req.POST.get('inputLog', ''):
            errors.append("Enter maintain log.")

        content = req.POST['inputLog']

        maintainLog=MaintainLog(MachineName=device.name,user=currentuser.get_full_name(),timestamp=timezone.now(),content=content)
        maintainLog.save()

        #return render("mainLog.html",{"maintainLog":maintainLog})
        return HttpResponseRedirect(reverse('mainLog',args= (id,)))

    msg=""
    content = "123"
    print content
    print device.name

    # maintainLogs = MaintainLog.objects.filter(MachineName=device.name).order_by("-timestamp")
    
    # maintainLogOB = MaintainLog.objects.filter(MachineName__startswith="OB").order_by("-timestamp")
    # maintainLogBC = MaintainLog.objects.filter(MachineName__startswith="BC").order_by("-timestamp")
    # maintainLogPDU = MaintainLog.objects.filter(MachineName__startswith="PDU").order_by("-timestamp")
    # maintainLogIOHOST = MaintainLog.objects.filter(MachineName__startswith="IOHOST").order_by("-timestamp")
    # maintainLogBEARCAT = MaintainLog.objects.filter(MachineName__startswith="BEARCAT").order_by("-timestamp")
    
    # print maintainLog.MachineName
    maintainlog = MaintainLog.objects.filter(MachineName=device.name).order_by("-timestamp")
    # maintainLogOB2004 = MaintainLog.objects.filter(MachineName="OB-S2004").order_by("-timestamp")
    # maintainLogOB2005 = MaintainLog.objects.filter(MachineName="OB-S2005").order_by("-timestamp")
    # maintainLogOB2006 = MaintainLog.objects.filter(MachineName="OB-S2006").order_by("-timestamp")
    # maintainLogOB2007 = MaintainLog.objects.filter(MachineName="OB-S2007").order_by("-timestamp")
    # maintainLogOB2008 = MaintainLog.objects.filter(MachineName="OB-S2008").order_by("-timestamp")
    # maintainLogOB2009 = MaintainLog.objects.filter(MachineName="OB-S2009").order_by("-timestamp")
    # maintainLogOB2010 = MaintainLog.objects.filter(MachineName="OB-S2010").order_by("-timestamp")
    # maintainLogOB2011 = MaintainLog.objects.filter(MachineName="OB-S2011").order_by("-timestamp")
    # maintainLogOB2012 = MaintainLog.objects.filter(MachineName="OB-S2012").order_by("-timestamp")
    # maintainLogOB2013 = MaintainLog.objects.filter(MachineName="OB-S2013").order_by("-timestamp")
    # maintainLogOB2014 = MaintainLog.objects.filter(MachineName="OB-S2014").order_by("-timestamp")


    # maintainLogBC1000 = MaintainLog.objects.filter(MachineName="BC-Z1000").order_by("-timestamp")
    # maintainLogBC1009 = MaintainLog.objects.filter(MachineName="BC-Z1009").order_by("-timestamp")

    # maintainLogPDU1 = MaintainLog.objects.filter(MachineName="PDU port1").order_by("-timestamp")
    # maintainLogPDU2 = MaintainLog.objects.filter(MachineName="PDU port2").order_by("-timestamp")
    # maintainLogPDU3 = MaintainLog.objects.filter(MachineName="PDU port3").order_by("-timestamp")
    # maintainLogPDU4 = MaintainLog.objects.filter(MachineName="PDU port4").order_by("-timestamp")
    # maintainLogPDU5 = MaintainLog.objects.filter(MachineName="PDU port5").order_by("-timestamp")
    # maintainLogPDU6 = MaintainLog.objects.filter(MachineName="PDU port6").order_by("-timestamp")
    # maintainLogPDU7 = MaintainLog.objects.filter(MachineName="PDU port7").order_by("-timestamp")
    # maintainLogPDU8 = MaintainLog.objects.filter(MachineName="PDU port8").order_by("-timestamp")

    # maintainLogIO1 = MaintainLog.objects.filter(MachineName="IO-Host-KVM-Linux-1").order_by("-timestamp")
    # maintainLogIO2 = MaintainLog.objects.filter(MachineName="IO-Host-KVM-Linux-2").order_by("-timestamp")
    # maintainLogIO3 = MaintainLog.objects.filter(MachineName="IO-Host-KVM-Win-1").order_by("-timestamp")

    # maintainLogBE00 = MaintainLog.objects.filter(MachineName="BEARCAT-00").order_by("-timestamp")
    # maintainLogBE01 = MaintainLog.objects.filter(MachineName="BEARCAT-01").order_by("-timestamp")
    # maintainLogBE02 = MaintainLog.objects.filter(MachineName="BEARCAT-02").order_by("-timestamp")
    # maintainLogBE03 = MaintainLog.objects.filter(MachineName="BEARCAT-03").order_by("-timestamp")
    # maintainLogBE04 = MaintainLog.objects.filter(MachineName="BEARCAT-04").order_by("-timestamp")
    # maintainLogBE05 = MaintainLog.objects.filter(MachineName="BEARCAT-05").order_by("-timestamp")
    # maintainLogBE06 = MaintainLog.objects.filter(MachineName="BEARCAT-06").order_by("-timestamp")
    # maintainLogBE07 = MaintainLog.objects.filter(MachineName="BEARCAT-07").order_by("-timestamp")
    # maintainLogBE08 = MaintainLog.objects.filter(MachineName="BEARCAT-08").order_by("-timestamp")
    # maintainLogBE09 = MaintainLog.objects.filter(MachineName="BEARCAT-09").order_by("-timestamp")
    # maintainLogBE10 = MaintainLog.objects.filter(MachineName="BEARCAT-10").order_by("-timestamp")
    # maintainLogBE11 = MaintainLog.objects.filter(MachineName="BEARCAT-11").order_by("-timestamp")


    # print maintainLogOB2004
    

    # context={'maintainLogOB2004': maintainLogOB2004,
    #             'maintainLogOB2005': maintainLogOB2005,
    #             'maintainLogOB2006': maintainLogOB2006,
    #             'maintainLogOB2007': maintainLogOB2007,
    #             'maintainLogOB2008': maintainLogOB2008,
    #             'maintainLogOB2009': maintainLogOB2009,
    #             'maintainLogOB2010': maintainLogOB2010,
    #             'maintainLogOB2011': maintainLogOB2011,
    #             'maintainLogOB2012': maintainLogOB2012,
    #             'maintainLogOB2013': maintainLogOB2013,
    #              'maintainLogOB2014': maintainLogOB2014,
    #             'maintainLogBC1000': maintainLogBC1000,
    #             'maintainLogBC1009': maintainLogBC1009,

    #             'maintainLogPDU1':maintainLogPDU1,
    #             'maintainLogPDU2':maintainLogPDU2,
    #             'maintainLogPDU3':maintainLogPDU3,
    #             'maintainLogPDU4':maintainLogPDU4,
    #             'maintainLogPDU5':maintainLogPDU5,
    #             'maintainLogPDU6':maintainLogPDU6,
    #             'maintainLogPDU7':maintainLogPDU7,
    #             'maintainLogPDU8':maintainLogPDU8,

    #             'maintainLogIO1':maintainLogIO1,
    #             'maintainLogIO2':maintainLogIO2,
    #             'maintainLogIO3':maintainLogIO3,

    #             'maintainLogBE00':maintainLogBE00,
    #             'maintainLogBE01':maintainLogBE01,
    #             'maintainLogBE02':maintainLogBE02,
    #             'maintainLogBE03':maintainLogBE03,
    #             'maintainLogBE04':maintainLogBE04,
    #             'maintainLogBE05':maintainLogBE05,
    #             'maintainLogBE06':maintainLogBE06,
    #             'maintainLogBE07':maintainLogBE07,
    #             'maintainLogBE08':maintainLogBE08,
    #             'maintainLogBE09':maintainLogBE09,
    #             'maintainLogBE10':maintainLogBE10,
    #             'maintainLogBE11':maintainLogBE11,

    #             'device': device,
          
    #         }
    context={   'maintainlog': maintainlog,
                'usagelog' : usagelog,
                'device': device,
                'tab' : tabOption,
                'currentuser':currentuser
            }

    # context={'maintainLogs', maintainLogs}
    
    # if maintainLogOB2004.== device.name:
    #     print "OK"

    return render(req, "maintainLog.html",context)


def delete(req):

    if req.method == 'POST':
        print "i am here"
        willBeDel = req.POST.getlist("_selected_action")
        #get machine id for redirect
        log = MaintainLog.objects.get(id=willBeDel[0])
        device = Device.objects.get(name=log.MachineName)
        direcrUrl = "/labsmith/mainLog/" + str(device.id) + "/"

        for logid in willBeDel:
            log = MaintainLog.objects.get(id=logid)
            log.delete()

    return HttpResponseRedirect(direcrUrl)

@login_required(login_url="/login/")
def reserve_slicsfp(req):
    currentuser = req.user
    print currentuser
    info = []
    if req.method == 'POST':
        index = req.POST['deviceId']
        device = SlicSfp.objects.get(id=index)
    
        oldreservednumber = device.reserved_number
        newnumber = req.POST['slicsfpNum']
        availnumber = int(device.total_number)-int(device.reserved_number)
        if int(newnumber) > int(availnumber):
            newnumber = int(availnumber)
        newreservednumber = int(oldreservednumber)+int(newnumber)

        if int(newreservednumber) > int(device.total_number):
            newreservednumber = device.total_number
        device.reserved_number = newreservednumber
        device.save()
        # leftnumber = int(device.total_number)-int(device.reserved_number)
        if int(newreservednumber) > int(oldreservednumber):
            info=SlicSfpInfo(MachineName=device.model_name,user=currentuser.get_full_name(),time=timezone.now(),reserve_number=newnumber)
            info.save()
    return redirect('/labsmith/?tab=SLIC|SFP')


def release_slicsfp(req):
    currentuser = req.user
    print currentuser
    errors = []
    if req.method == 'POST':
        if not req.POST.get('info', ''):
            errors.append("Please enter remarks.For example: Leon returned 1.")    
        if not errors:
            index = req.POST['deviceId']
            device = SlicSfp.objects.get(id=index)
            oldreservednumber = device.reserved_number
            newnumber = req.POST['slicsfpNum']
            if int(newnumber) > int(oldreservednumber):
                newnumber = oldreservednumber
            availnumber = int(oldreservednumber) - int(newnumber)

            if int(availnumber) < 0:
                availnumber = 0
            device.reserved_number = availnumber
            device.info = req.POST['info']    
            device.save()
        # leftnumber = int(device.total_number)-int(device.reserved_number)
        if int(availnumber) < int(oldreservednumber):
            comment=SlicSfpInfo(MachineName=device.model_name,user=currentuser,time=timezone.now(),release_number=newnumber,info=device.info)
            comment.save()
        return redirect('/labsmith/?tab=SLIC|SFP')

def RackLayout(req):

    currentuser = req.user
    if(req.GET.has_key('tab')):
        tabOption = req.GET['tab']
    else:
        tabOption = 'Rack 1'
       
    context = {
               'tab' : tabOption,
    }
   
    return render(req,"RackLayout.html",context)

def pxeGuide(req):
    context=[]
    return render(req,"pxeGuide.html",context)
