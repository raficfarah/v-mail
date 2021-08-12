from django.test import TestCase
from emailsender.core.models import Message
from datetime import datetime


class MessageModelTest(TestCase):
    def setUp(self):
        self.obj = Message(
            sender='Rafic',
            receiver='Sandro',
            email='teste@gmail.com',
            content='blablabla'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Message.objects.exists())

    def test_created_at(self):
        '''Subscription must have an auto created_at attr.'''
        self.assertIsInstance(self.obj.created_at, datetime)