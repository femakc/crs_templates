from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'author',
        'text',
        'pub_date'
    ]
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
