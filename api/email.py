from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def send_message_email(email, receiver):
    subject = 'Alcohol Tracker Newsletter'
    sender = settings.EMAIL_HOST_USER

    text_content = render_to_string('email/message.txt', {"email": email})
    html_content = render_to_string('email/message.html', {"email": email})

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()