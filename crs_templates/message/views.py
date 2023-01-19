# from django.http import HttpResponse
from django.shortcuts import render
from .models import Message
from django.views.generic.edit import CreateView
from .forms import MessageForm
from django.urls import reverse_lazy


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
    success_url = reverse_lazy('message:index')
    
    def form_valid(self, form):
        form.test_celery()
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs): # Добавить отправку сообщения о регистрации
    #     return super().post(request, *args, **kwargs)
