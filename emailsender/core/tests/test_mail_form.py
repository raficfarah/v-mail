from django.core import mail
from django.test import TestCase
from emailsender.core.forms import MessageForm
from emailsender.core.models import Message


class MessageValidPost(TestCase):
    def setUp(self):
        self.data = dict(sender='rafic', receiver='sandro',
                         email='teste@gmail.com', content='blablabla blablabla')
        self.resp = self.client.post('', self.data)
        self.email = mail.outbox[0]

    def test_post(self):
        '''Valid POST should redirect to "/" '''
        self.assertEqual(302, self.resp.status_code)

    def test_send_message_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_message_email_subject(self):
        expect = 'Você recebeu uma carta!'
        self.assertEqual(expect, self.email.subject)

    def test_message_email_from(self):
        expect = 'elegante.correios.01@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_message_email_to(self):
        expect = ['elegante.correios.01@gmail.com', 'teste@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_message_email_body(self):
        contents = [
            'rafic',
            'sandro',
            'blablabla'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

    def test_save_message(self):
        self.assertTrue(Message.objects.exists())


class MessageInvalidPost(TestCase):
    def setUp(self):
        self.resp = self.client.post('', {})
        self.form = self.resp.context['message']

    def test_post(self):
        '''Invalid POST should not redirect.'''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_has_form(self):
        self.assertIsInstance(self.form, MessageForm)

    def test_form_has_errors(self):
        self.assertTrue(self.form.errors)

    def test_dont_save_message(self):
        self.assertFalse(Message.objects.exists())


class MessageSuccessNotification(TestCase):
    def setUp(self):
        self.data = dict(sender='rafic', receiver='sandro',
                         email='teste@gmail.com', content='blablabla blablabla')
        self.resp = self.client.post('', self.data, follow=True)

    def test_message(self):
        self.assertContains(self.resp, 'Sua carta foi enviada!')
