from django.db import models


class Message(models.Model):
    sender = models.CharField('nome do remetente', max_length=65, blank=True)
    receiver = models.CharField('nome do destinatário', max_length=65)
    email = models.EmailField('e-mail do destinatário', default=None)
    content = models.TextField('mensagem')
    created_at = models.DateTimeField('hora de envio', auto_now_add=True)
    
    class Meta:
        verbose_name = "mensagem"
        verbose_name_plural = "mensagens"
        ordering = ('-created_at',)

    def __str__(self):
        return self.receiver
