# from django.http import HttpResponse
from django.shortcuts import render
from .models import Message
from django.views.generic.edit import CreateView
from .forms import MessageForm


def index(request):
    template = 'message/index.html'
    prod_name = 'CRS'
    messages = Message.objects.order_by('-pub_date')[:10]
    context = {
        'template': template,
        'prod_name': prod_name,
        'messages': messages,
    }
    return render(request, template, context)


class MessageView(CreateView):
    form_class = MessageForm
    template_name = 'message/new_message.html'
    success_url = 'message/index.html'
