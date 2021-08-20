from emailsender.core.models import Message
from django.contrib import admin


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['receiver', 'sender', 'created_at',]
    fields = ['sender', 'receiver', 'email', 'content']