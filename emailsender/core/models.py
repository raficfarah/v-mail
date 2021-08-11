from django.db import models
from django.utils.timezone import now


class Message(models.Model):
    sender = models.CharField('remetente', max_length=65, blank=True)
    receiver = models.CharField('destinatário', max_length=65)
    email = models.EmailField('e-mail do destinatário', default=None)
    content = models.TextField()
    created_at = models.DateTimeField('hora de envio', default=now)
    
    class Meta:
        verbose_name = "mensagem"
        verbose_name_plural = "mensagens"
        ordering = ('-created_at',)

    def __str__(self):
        return self.sender
