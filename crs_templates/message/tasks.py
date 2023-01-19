from time import sleep
# from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_feedback_email_task(message):
    """Sends an email when the feedback form has been submitted."""
    sleep(20)
    return message
