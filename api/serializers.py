from rest_framework import serializers
from .models import NewsLetterRecipient


class NewsLetterRecipientSerializer(serializers.ModelSerializer):
  
    class Meta:
        ''' Meta class to map serializer's fields with model fields '''
        model = NewsLetterRecipient
        fields = ('id', 'email', 'date_registered')
        read_only_fields = ('date_registered',)
    