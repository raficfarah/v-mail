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
        tags = (
            ('<form', 1),
            ('<input', 5),
            ('<textarea', 1),
            ('type="text"', 2),
            ('type="email"', 1),
            ('type="submit"', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        '''Html must contain a CSRF token.'''
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        '''Context must have MessageForm'''
        self.assertIsInstance(self.form, MessageForm)

    def test_form_has_fields(self):
        expected = ['sender', 'receiver', 'email', 'content']
        self.assertSequenceEqual(expected, list(self.form.fields))
