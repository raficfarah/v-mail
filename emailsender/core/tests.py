from django.core import mail
from django.test import TestCase
from emailsender.core.forms import MessageForm


class SendMessageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('')
        self.form = self.resp.context['message']

    def test_get(self):
        '''Get "/" must return status code 200.'''
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        '''Must use index.html'''
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_html(self):
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 5)
        self.assertContains(self.resp, '<textarea', 1)
        self.assertContains(self.resp, 'type="text"', 2)
        self.assertContains(self.resp, 'type="email"', 1)
        self.assertContains(self.resp, 'type="submit"', 1)

    def test_csrf(self):
        '''Html must contain a CSRF token.'''
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        '''Context must have MessageForm'''
        self.assertIsInstance(self.form, MessageForm)

    def test_form_has_fields(self):
        self.assertSequenceEqual(
            ['sender', 'receiver', 'email', 'content'], list(self.form.fields))


class MessagePostTest(TestCase):
    def setUp(self):
        self.data = dict(sender='rafic', receiver='sandro',
                         email='sandrohmt@gmail.com', content='blablabla blablabla')
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
        expect = ['raficfarah07@gmail.com', 'sandrohmt@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_message_email_body(self):
        self.assertIn('rafic', self.email.body)
        self.assertIn('sandro', self.email.body)
#       self.assertIn('sandrohmt@gmail.com', self.email.body)
        self.assertIn('blablabla', self.email.body)


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


class MessageSuccessNotification(TestCase):
    def setUp(self):
        self.data = dict(sender='rafic', receiver='sandro',
                         email='sandrohmt@gmail.com', content='blablabla blablabla')
        self.resp = self.client.post('', self.data, follow=True)

    def test_message(self):
        self.assertContains(self.resp, 'Sua carta foi enviada!')
