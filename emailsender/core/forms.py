from emailsender.core.models import Message
from django import forms


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'nome@exemplo.com'})
        }
        fields = ['sender', 'receiver', 'email', 'content']
    