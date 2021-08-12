from django.test import TestCase
from emailsender.core.forms import MessageForm


class MessageGet(TestCase):
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


