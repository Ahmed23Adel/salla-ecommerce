

from urllib.parse import urljoin
from django.utils.encoding import *
from django.utils.http import *
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        print(user)
        return (
                user.data['email']
        )


email_verification_token = EmailVerificationTokenGenerator()


def send_verification_email(from_email, from_name, user):
    link = settings.BASE_URL_FOR_EMAIL_VERFICATION_CUSTOM
    key = os.getenv('SALLA_DJANGO_EMAIL_VERIFICATION_KEY')
    fernet = Fernet(key)
    uid_linker =  fernet.encrypt(str(user['id']).encode()).decode("utf-8") 
    subject = 'Email verification (Please do not reply)'
    message = f'Hi {from_name}, thank you for registering in salla e commerce.\n \
        For seucity reasons; we need to verify your email. please click that link for confirmation.\n \
            {urljoin(link, str(uid_linker))} \n \
            please ignore it if you have not tried to register for salla website, however we encourge you to do so. \
            \n Thanks, \
            \n Salla.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [from_email]
    send_mail( subject, message, email_from, recipient_list ) 



def decode_verficiation_link(frnt_rec):
    key = os.getenv('SALLA_DJANGO_EMAIL_VERIFICATION_KEY')
    fernet = Fernet(key)
    return fernet.decrypt(frnt_rec).decode()