from django import forms
# from time import sleep
from .models import Message
from .tasks import send_feedback_email_task


class MessageForm(forms.ModelForm):

    def test_celery(self):
        send_feedback_email_task.delay('!!! GOOD !!!')

    class Meta:
        model = Message
        fields = ('author', 'text')
