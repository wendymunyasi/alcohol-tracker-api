from django.db import models
import datetime


class NewsLetterRecipient(models.Model):

    'A model for the newsletter recipients'
    email = models.EmailField(unique=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_registered']

    def __str__(self):
        ''' convert the object to a string. '''

        return '{} registered on {}'.format(self.email, self.date_registered)
    
    @classmethod
    def get_newsletter_recipients(cls):
        ''' method to fetch all newsletter recipients from the database '''
        recipients = cls.objects.all()
        
        return recipients
