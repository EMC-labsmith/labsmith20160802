from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone
from post_office.models import EmailTemplate
from post_office import mail
from django.core.mail import EmailMultiAlternatives
import os

from device_management.models import Device, UsageLog

EXPIRED_DAYS = 30
# CC_MAIL = 'leon.li@emc.com'
CC_MAIL = 'tianyang.li@emc.com'
VALID_DEVICE_HEADERS = ['OB-S', 'BC', 'JF', 'MT', 'VX', 'BR', 'OB DAE', 'IO', 'KVM']
SENDER = 'LabSmith@noreplay.emc.com'
EMAIL_TEMPLATE_PATH = '../../../templates/hold_reminder.html'
EMAIL_TEMPLATE_NAME = 'hold_reminder'


class Command(BaseCommand):
    help = 'Check all devices and find if the holding time is larger than %d days, then sent an email notification to device owner.' % EXPIRED_DAYS

    def add_arguments(self, parser):
        parser.add_argument('-s', '--send_mail', action='store_true')
        parser.add_argument('-c', '--cc', default=CC_MAIL)

    def handle(self, *args, **options):
        # Update email template
        foundTemplates = [t for t in EmailTemplate.objects.filter(name__exact=EMAIL_TEMPLATE_NAME)]

        if not foundTemplates:
            script_dir = os.path.dirname(__file__)
            filename = os.path.join(script_dir, EMAIL_TEMPLATE_PATH)
            filename = os.path.abspath(os.path.realpath(filename))

            with open(filename, 'r') as fh:
                html_context = fh.read()

            EmailTemplate.objects.create(
                name=EMAIL_TEMPLATE_NAME,
                subject='LabSmith Email Notification ({{user.get_full_name}}): Holding Time Reminder.',
                content=html_context,
                html_content=html_context,
            )
        elif len(foundTemplates) > 1:
            [t.delete() for t in foundTemplates[:-1]]

        # Update Holding Time
        devices = Device.objects.all()

        for device in devices:
            if hasattr(device, 'owner') and device.owner and not device.lock:
                try:
                    usagelog = UsageLog.objects.get(machineName=device.name, port=device.port, user=device.owner.get_full_name(), isUse='f')
                    if usagelog:
                        device.holdingTime = (timezone.now() - usagelog.reserveTimestamp).days + 1
                        device.save()
                except:
                    continue
            else:
                device.holdingTime = ''
                device.save()

        # Render and send mail
        users = User.objects.all()
        for user in users:
            foundDevices = Device.objects.filter(owner__id__exact=user.id)
            foundDevices = [device for device in foundDevices if device.holdingTime and int(device.holdingTime) > EXPIRED_DAYS]
            if not foundDevices:
                continue
            foundDevices = [device for device in foundDevices if [header for header in VALID_DEVICE_HEADERS if device.name.startswith(header)]]
            if not foundDevices:
                continue
            # user.email
            # mail.send(sender='tianyang.li@emc.com', recipients='tianyang.li@emc.com', template='holding_reminder', context={'user': user, 'devices': foundDevices})
            print user, foundDevices
            mailObj = mail.send(sender=SENDER, recipients=['tianyang.li@emc.com', ], template='hold_reminder', context={'user': user, 'devices': foundDevices})
            msg = EmailMultiAlternatives(mailObj.subject, "html", mailObj.from_email, mailObj.to)
            msg.attach_alternative(mailObj.html_message, "text/html")
            msg.send()
            # exit()

        self.stdout.write(self.style.SUCCESS('Successfully run check expired.'))
