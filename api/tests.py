from django.test import TestCase
from .models import NewsLetterRecipient


class NewsLetterRecipientTestCase(TestCase):

    ''' Test case for the newsletter recipients model '''

    def setUp(self):
        self.new_newsletter_recipient = NewsLetterRecipient(email="damon@gmail.com")
        self.new_newsletter_recipient.save()

    def tearDown(self):
        ''' test to run before every test case '''
        NewsLetterRecipient.objects.all().delete()

    def test_newsletter_recipient_instance(self):
        ''' test to see if a newsletter recipient instance was created correctly '''
        self.assertTrue(isinstance(self.new_newsletter_recipient, NewsLetterRecipient))

    def test_save_newsletter_recipient(self):
        ''' test to see if a newsletter recipient was saved correctly '''
        self.test_newsletter_recipient = NewsLetterRecipient( email="damon@gmail.com")
        self.test_newsletter_recipient.save()
        newsletter_recipients = NewsLetterRecipient.objects.all().count()
        self.assertTrue(newsletter_recipients == 2)